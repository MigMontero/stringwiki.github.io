---
title: 'Maxima'
---

# Maxima

[Maxima](http://maxima.sourceforge.net/) is an open source computer algebra system, similar to Mathematica.  It is available for GNU/Linux, MacOS X and Windows.

### installation on a GNU/Linux system
There should be pre-compiled packages available for most distributions.  For example in Debian-based distributions such as [Ubuntu](http://www.ubuntu.com/) install the maxima and maxima-share packages by typing
<pre>
sudo apt-get install maxima maxima-share
</pre>

### sample usage
<pre>
expand((x+y+z)^4);
integrate(1/(1+x^3),x);
</pre>

### tensor manipulation
The [ctensor module](http://maxima.sourceforge.net/docs/manual/en/maxima_28.html) is useful for tensor manipulation (in Ubuntu GNU/Linux this is included in the maxima-share package).

Sample usage:
<pre>
load(ctensor);
dim: 5;
ct_coords: [t,rho,chi1,chi2,chi3];
lg: matrix([-(R^2)*(cosh(rho)^2),0,0,0,0],[0,R^2,0,0,0],[0,0,(R^2)*(sinh(rho)^2),0,0],[0,0,0,(R^2)*(sinh(rho)^2)*sin(chi1)^2,0],[0,0,0,0,(R^2)*(sinh(rho)^2)*(sin(chi1)^2)*(sin(chi2)^2)]);
cmetric();
ug;
christof(mcs);
ricci(true);
scurvature();
trigsimp(%);
</pre>
This finds the Christoffel symbols, the Ricci tensor and the Ricci curvature scalar of the 5-dimensional Anti de Sitter spacetime metric.

### plotting with Maxima
Maxima integrates well with [gnuplot](http://www.gnuplot.info/) to provide graph plotting. (Note that in Ubuntu GNU/Linux you need the addition package gnuplot-x11 or the GUI wxMaxima to use gnuplot's full graphical output) 

A selection of examples:
<pre>
plot2d(sin(x),[x,0,10]);
plot2d([parametric, (1+cos(t))*cos(t), (1+cos(t))*sin(t), [t,-%pi,%pi], [nticks,80]],[x, -1,2]);
plot3d (atan (-x^2 + y^3/4), [x, -4, 4], [y, -4, 4], [grid, 50, 50]);
</pre>
For more examples see [Maxima manual: plotting](http://maxima.sourceforge.net/docs/manual/en/maxima_8.html).

### integration with GNU Emacs
There is a Maxima-mode for GNU Emacs.  For Ubuntu GNU/Linux simply install the maxima-emacs package.  So that GNU Emacs knows to use this mode when you edit files with the .max extension, add the following lines to your .emacs file in your home directory:
<pre>
(setq auto-mode-alist (cons '("\\.max" . maxima-mode) auto-mode-alist))
(setq load-path (cons  "/usr/share/maxima/5.9.2/emacs" load-path ))
(autoload 'maxima "maxima" "Running Maxima interactively" t)
(autoload 'maxima-mode "maxima" "Maxima editing mode" t)
</pre>

### links
[Maxima website](http://maxima.sourceforge.net/)

[Maxima manual](http://maxima.sourceforge.net/docs/manual/en/maxima.html)

[Maxima tutorial](http://maxima.sourceforge.net/docs/tutorial/en/gaertner-tutorial-revision/Contents.htm)

[Introduction to Maxima](http://maxima.sourceforge.net/docs/intromax/intromax.html)
