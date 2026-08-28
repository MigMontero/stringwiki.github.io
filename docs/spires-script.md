---
title: 'SPIRES script'
---

# SPIRES script

SPIRES script is a program written in the [python](http://www.python.org/) programming language that accesses information on papers in the [SPIRES](http://www.slac.stanford.edu/spires/) online high energy physics literature database.  It can access title, author, bibitem and [BiBTeX](references-with-bibtex.md) records, update your local BiBTeX library and download papers from the [arXiv](http://www.arxiv.org/).  A separate program listcitations.py reads through a TeX file and then looks up all the \cite{...} references and outputs the bibitems.  Although originally written for the GNU/Linux command line, the code should be portable enough to run on any operating system with a python interpreter.

### download
Download [spires.py](spires-py.md) and [listcitations.py](listcitations-py.md).

### installation on a GNU/Linux system
The script requires the python interpreter to be installed on your system.  This is automatically installed on most GNU/Linux distributions, but check it is there by typing
<pre>
python
</pre>
at the command line and see what happens.

If python is present download [spires.py](spires-py.md) and run it by typing
<pre>
python spires.py hep-th/9711200
</pre>

### usage
The typical accepted inputs are the usual arXiv references, the SPIRES TeX key or a SPIRES-style journal reference
<pre>
python spires.py hep-th/9711200
python spires.py 0705.0303
python spires.py Maldacena:1997re
python spires.py CMPHA,43,199
python spires.py Phys.Rev.,D52,5783
</pre>

If no options are specified all possible outputs will be displayed
<pre>
tom@fyodor:~$ python spires.py hep-th/9711200
@Article{Maldacena:1997re,
     author    = "Maldacena, Juan M.",
     title     = "The large N limit of superconformal field theories and
                  supergravity",
     journal   = "Adv. Theor. Math. Phys.",
     volume    = "2",
     year      = "1998",
     pages     = "231-252",
     eprint    = "hep-th/9711200",
     SLACcitation  = "%%CITATION = HEP-TH/9711200;%%"
}
Maldacena, Juan M.
The large N limit of superconformal field theories and supergravity
\cite{Maldacena:1997re}
</pre>

To see all the options access the help page
<pre>
tom@fyodor:~$ python spires.py -h
SPIRES script
Usage:
python spires.py reference [ -hbiatcev ] [ --help ] [ --library library.bib ] [ --download download_path/ ]
"reference" must be a standard arXiv reference, e.g. hep-th/9711200, 0705.0303, Maldacena:1997re or a SPIRES journal reference, e.g. CMPHA,43,199
Options:
-h, --help
displays this help message
-b
displays the BiBTeX entry
-i
displays the bibitem entry
-a
displays the author(s)
-t
displays the title
-c
displays the TeX citation key
-e
displays everything
-v
verbose mode

--download download_path/
for arXiv references downloads a pdf of the paper from the arXiv to the directory download_path/
--library library.bib
if it is not already in library.bib, appends the BiBTeX entry to library.bib; use at your own risk
</pre>

Each item can be specified individually with switches, e.g. -t for title, -a for authors, -b for BiBTeX entry, -c for SPIRES TeX key.  For example
<pre>
tom@fyodor:~$ python spires.py hep-th/9711200 -at
Maldacena, Juan M.
The large N limit of superconformal field theories and supergravity
</pre>

If you have a BiBTeX database file such as library.bib then the script can update the file with the BiBTeX entry if it is not already present
<pre>
python spires.py hep-th/9711200 --library library.bib
</pre>

To download a PDF of an eprint from the [arXiv](http://www.arxiv.org/) to the directory <code>some_folder/</code>
<pre>
python spires.py hep-th/9711200 --download some_folder/
</pre>

### listcitations.py
To use this program you must download [spires.py](spires-py.md) and [listcitations.py](listcitations-py.md) into the same directory.

This program reads a TeX file and then looks up all the \cite{...} references and outputs the bibitems. The typical accepted inputs are the usual arXiv references, the SPIRES TeX key or a SPIRES-style journal reference.  With no options it will output bibitems
<pre>
python listcitations.py tex_file.tex
</pre>
It can also output BiBTeX entries instead
<pre>
python listcitations.py tex_file.tex -b
</pre>
To see all the options access the help page
<pre>
tom@tarkovsky:~$ python listcitations.py -h
list citations script
Usage:
python listcitations.py TeX_file_name.tex [ -hbiv ] [ --help ]

TeX_file_name must contain citations as standard arXiv references,
e.g. hep-th/9711200, 0705.0303, Maldacena:1997re or SPIRES journal
references, e.g. CMPHA,43,199

Options:
-h, --help
displays this help message
-b
displays the BiBTeX entry
-i
displays the bibitem entry
-v
verbose mode
</pre>

### future features

* allow alias citations such as \cite{mypaper} for listcitations.py

### technical details
The code is very modular so it is easy to write your own programs using the functions defined in spires.py.  Just import the functions in spires.py with <code>import spires</code>; you can use spires.py as a library of SPIRES-related functions (see [listcitations.py](listcitations-py.md) as an example).

### comments and bugs
If you have any comments or find bugs, please contact Tom.

### thanks
Thanks to Travis C. Brooks of [SPIRES](http://www.slac.stanford.edu/spires/) for his help and [Kevin Goldstein](http://theory.tifr.res.in/~kevin/) for pointing out the python <code>urllib</code> library.

### licence
This script is Copyright 2007 Tom Brown and made available under the [GNU General Public Licence](http://www.gnu.org/copyleft/gpl.html).
