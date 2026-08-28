---
title: 'Processing LaTeX with GNU/Linux systems'
---

# Processing LaTeX with GNU/Linux systems

Suppose you have a file <code>sample.tex</code> written in LaTeX and you want to process it into a readable document on a GNU/Linux system.

To convert it into a DVI file go to a command line and move to the directory in which you saved the file.  There run
 latex sample.tex
Unless there is a problem you should now find a file called <code>sample.dvi</code> in the directory.

To convert this into a PS postscript file which you can then print run 
 dvips sample.dvi

To convert this into a PDF file run
 ps2pdf sample.ps

To convert a LaTeX file <code>sample.tex</code> directly into a PDF file run 
 pdflatex sample.tex
