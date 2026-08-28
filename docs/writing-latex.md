---
title: 'Writing LaTeX'
---

# Writing LaTeX

There are many excellent introductions to writing mathematics with LaTeX, for example [Introduction to LaTeX](http://www.math.uiuc.edu/~hildebr/tex/course/).  Below is a quick and dirty example to start with.

LaTeX is the language in which most mathematics and physics documents
are written.  Mathematical symbols and equations are written in a
special markup.  For example an integral sign is inserted with
<code>\int</code>.  The best way to learn LaTeX is by example.  Here
is a basic LaTeX file:

 \documentclass[a4paper,10pt]{article}
 \usepackage{amsfonts,amsthm,amsmath,amssymb}
 \title{Simple example} 
 
 \begin{document}
 \maketitle
  
 \section{Quadratic equation}
 
 We want to solve $ax^2+bx+c$.  The solution is
 \begin{equation}
   x= \frac{-b\pm \sqrt{b^2 -4ac}}{2a}
 \end{equation}
 
 \end{document}

LaTeX commands start with a back slash <code>\</code>. Sometimes they
have an argument in curly brackets, e.g <code>\sqrt{b^2-4ac}</code>.  Most of the commands in the document above are self-explanatory.

To convert this into a readable document first save it into a file
with a <code>.tex</code> extension, e.g. <code>sample.tex</code>.
Then you need to process it.  If you are using GNU/Linux, see
[Processing LaTeX with GNU/Linux systems](processing-latex-with-gnu-linux-systems.md).

### links
[Introduction to LaTeX](http://www.math.uiuc.edu/~hildebr/tex/course/)

[LaTeX: from quick and dirty to style and finesse](http://ricardo.ecn.wfu.edu/LaTeX/)

[LaTeX Tips](http://www.math.uiuc.edu/~hildebr/tex/basics.html)
