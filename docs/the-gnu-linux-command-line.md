---
title: 'The GNU/Linux command line'
---

# The GNU/Linux command line

### basics
<pre>
ls -lrt
</pre>
lists the contents of a directory with full details (l) in reverse (r) time order (t)

### archiving
<pre>
tar -xvzf some_archive_to_be_extracted.tar.gz 
</pre>
this extracts (x) some_archive_to_be_extracted.tar.gz which is zipped (z); the command will talk to you (v) and won't bother you with further options (f)
<pre>
tar -cpvzf some_archive_to_be_created.tar.gz /path/to/archive
</pre>
will create (c) an archive file some_archive_to_be_created.tar.gz from the contents of /path/to/archive; it will zip it (z), preserve permissions (p), the command will talk to you (v) and won't bother you with further options (f)

### printing
[http://www.colorado.edu/its/docs/unix/moreprint.html] is a useful resource for printing in Unix
<pre>
lpr -Pprinter_name file.ps
</pre>
prints file.ps
<pre>
psnup -2 single.ps double.ps 
</pre>
takes single.ps and makes double.ps with two pages of single.ps on each page of double.ps
<pre>
psselect -p3-10 file.ps selection.ps
</pre>
selects pages 3 to 10 out of file.ps and creates double.ps with this 8 pages
