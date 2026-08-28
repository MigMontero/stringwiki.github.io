#!/usr/bin/env python3
"""Convert the current revision of selected MediaWiki pages to MkDocs Markdown.

This is deliberately dependency-free and repeatable. It preserves the supplied
export as the source of truth while avoiding publication of the export itself.
"""

from __future__ import annotations

import argparse
import gzip
import html
import os
import re
import shutil
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

MW_NS = "{http://www.mediawiki.org/xml/export-0.11/}"
PUBLISHED_NAMESPACES = {"0", "4", "12"}


@dataclass
class Page:
    title: str
    namespace: str
    text: str
    redirect: str | None


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "untitled"


def page_path(title: str) -> Path:
    return Path("index.md") if title == "String Theory Wiki" else Path(f"{slugify(title)}.md")


def read_pages(source: Path) -> list[Page]:
    pages: list[Page] = []
    with gzip.open(source, "rb") as exported:
        for _, element in ET.iterparse(exported, events=("end",)):
            if element.tag != f"{MW_NS}page":
                continue
            namespace = element.findtext(f"{MW_NS}ns", default="")
            if namespace in PUBLISHED_NAMESPACES:
                revision = element.find(f"{MW_NS}revision")
                text = "" if revision is None else revision.findtext(f"{MW_NS}text", default="")
                redirect = element.find(f"{MW_NS}redirect")
                pages.append(
                    Page(
                        title=element.findtext(f"{MW_NS}title", default="Untitled"),
                        namespace=namespace,
                        text=text,
                        redirect=None if redirect is None else redirect.attrib.get("title"),
                    )
                )
            element.clear()
    return pages


def relative_markdown_link(source: Path, target: Path, anchor: str | None) -> str:
    destination = os.path.relpath(target, start=source.parent).replace(os.sep, "/")
    return destination + (f"#{slugify(anchor)}" if anchor else "")


def replace_internal_links(text: str, source: Path, paths: dict[str, Path]) -> str:
    def substitute(match: re.Match[str]) -> str:
        raw_target, label = (match.group(1).split("|", 1) + [None])[:2] if "|" in match.group(1) else (match.group(1), None)
        target, anchor = (raw_target.split("#", 1) + [None])[:2] if "#" in raw_target else (raw_target, None)
        label = label or target
        destination = paths.get(target)
        if destination is None:
            return label
        return f"[{label}]({relative_markdown_link(source, destination, anchor)})"

    return re.sub(r"\[\[([^\]]+)\]\]", substitute, text)


def convert_home_table(text: str) -> str:
    pattern = re.compile(
        r"\{\|[^\n]*\n\|-\n\|[^|\n]*\|\n(.*?)\n\|[^|\n]*\|\n(.*?)\n\|\}",
        re.DOTALL,
    )

    def substitute(match: re.Match[str]) -> str:
        # Keep the migration output ordinary Markdown. Markdown embedded in
        # HTML is fragile across renderers and was visible literally on some
        # previews; one readable topic list is preferable to two brittle ones.
        return match.group(1).strip() + "\n\n" + match.group(2).strip()

    return pattern.sub(substitute, text)


def convert_wikitext(text: str, source: Path, paths: dict[str, Path]) -> str:
    text = html.unescape(text.replace("\r\n", "\n"))
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"__(?:TOC|FORCETOC|NOTOC)__", "", text, flags=re.IGNORECASE)
    if source.name == "index.md":
        text = re.sub(
            r"A \[http://en\.wikipedia\.org/wiki/Wiki wiki\].*?"
            r"click on the \"edit\" tab at the top of the page\.",
            "This site is updated through GitHub pull requests. See "
            "[Contributing](contributing.md) to suggest a change.",
            text,
            flags=re.DOTALL,
        )
    text = convert_home_table(text)
    text = re.sub(r"<math>(.*?)</math>", lambda m: "\\(" + m.group(1).strip() + "\\)", text, flags=re.DOTALL | re.IGNORECASE)
    # A MediaWiki line commonly has '<br>' followed by its own newline. Consume
    # that source newline, otherwise Markdown sees an empty paragraph between
    # a conference name and its location/date.
    text = re.sub(r"<br\s*/?>[ \t]*(?:\n)?", "  \n", text, flags=re.IGNORECASE)

    def heading(match: re.Match[str]) -> str:
        level = max(2, min(6, len(match.group(1))))
        return "#" * level + " " + match.group(2).strip()

    text = re.sub(r"^(={2,6})\s*(.*?)\s*\1\s*$", heading, text, flags=re.MULTILINE)
    text = replace_internal_links(text, source, paths)
    text = re.sub(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]", r"[\2](\1)", text)

    # Convert MediaWiki list markers before converting bold text: the Markdown
    # bold delimiter '**' would otherwise look like a nested list marker when
    # it starts a line.
    def list_marker(match: re.Match[str]) -> str:
        return "  " * (len(match.group(1)) - 1) + "* "

    text = re.sub(r"^(\*+)(?=\S)", list_marker, text, flags=re.MULTILINE)

    # MediaWiki permits a list to begin directly after a sentence. Markdown
    # treats that as part of the paragraph, so insert a separating blank line
    # before each top-level list while leaving nested list items alone.
    separated_lines: list[str] = []
    for line in text.splitlines():
        if (
            line.startswith("* ")
            and separated_lines
            and separated_lines[-1].strip()
            and not re.match(r"^\s*\* ", separated_lines[-1])
        ):
            separated_lines.append("")
        separated_lines.append(line)
    text = "\n".join(separated_lines)

    text = re.sub(r"'''''(.*?)'''''", r"***\1***", text)
    text = re.sub(r"'''(.*?)'''", lambda m: f"**{m.group(1).strip()}**", text)
    text = re.sub(r"''(.*?)''", r"_\1_", text)
    return text.strip() + "\n"


def redirect_body(source: Path, target: Path) -> str:
    source_dir = source.with_suffix("").as_posix()
    target_dir = "" if target.name == "index.md" else target.with_suffix("").as_posix()
    relative_url = os.path.relpath(target_dir or ".", start=source_dir).replace(os.sep, "/")
    if relative_url == ".":
        relative_url = "./"
    elif not relative_url.endswith("/"):
        relative_url += "/"
    continue_link = relative_markdown_link(source, target, None)
    return (
        f'<meta http-equiv="refresh" content="0; url={relative_url}">\n\n'
        f"This page has moved. [Continue]({continue_link})\n"
    )


def write_pages(pages: list[Page], destination: Path) -> tuple[int, int]:
    paths = {page.title: page_path(page.title) for page in pages}
    redirects = 0
    for page in pages:
        output = destination / paths[page.title]
        output.parent.mkdir(parents=True, exist_ok=True)
        front_matter = f"---\ntitle: {page.title!r}\n---\n\n"
        if page.redirect and page.redirect in paths:
            body = redirect_body(paths[page.title], paths[page.redirect])
            redirects += 1
        else:
            body = f"# {page.title}\n\n" + convert_wikitext(page.text, paths[page.title], paths)
        output.write_text(front_matter + body, encoding="utf-8")
    return len(pages), redirects


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("docs"))
    args = parser.parse_args()
    pages = read_pages(args.source)
    if not pages:
        raise SystemExit("No publishable pages found in the MediaWiki export.")
    args.output.mkdir(parents=True, exist_ok=True)
    count, redirects = write_pages(pages, args.output)
    print(f"Converted {count} pages ({redirects} redirects) into {args.output}.")


if __name__ == "__main__":
    main()
