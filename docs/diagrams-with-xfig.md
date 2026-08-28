---
title: 'Diagrams with xfig'
---

# Diagrams with xfig

[xfig](http://www.xfig.org/) allows you to intuitively draw maths diagrams and output them as encapsulated Postscript (EPS) files for inclusion in LaTeX documents.

In xfig keep an eye on the top right of the window because it tells you what the buttons on the mouse do for the particular mode you're in.

### including diagrams in your LaTeX document
Once you have exported your diagram as an EPS file you now want to include it in a LaTeX document.  You must use the graphicx package by including at the top of the LaTeX file
<pre>
 \usepackage{graphicx}
</pre>
Include the figure torus.eps at the point of your choosing with
<pre>
\begin{figure}[t]
\begin{center}
\includegraphics[height=7cm,width=16cm]{torus}
\caption{ The torus } \label{fig:torus}
\end{center}
\end{figure}
</pre>
To resize the figure use \resizebox{!}{4.5in}{\includegraphics{torus.eps}} and to rotate it use \rotatebox{270}{\includegraphics{torus.eps}}.

### links
[xfig website](http://www.xfig.org/)

[xfig user manual](http://www.xfig.org/userman/)

[LaTeX Tips](http://www.math.uiuc.edu/~hildebr/tex/basics.html) has more information on including figures
