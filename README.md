# Linus Karlsson's PhD dissertation

This repository contains the TeX sources for my dissertation.
The sources should be compiled with LuaLaTeX and Biber.

To compile the dissertation from source, you also need the fonts Adobe Garamond Pro and Frutiger LT Std.
These are the profile fonts of Lund University, so if you are affiliated with the university you can [download them here](https://www.staff.lu.se/support-and-tools/communication-and-graphic-profile/download-templates-and-communication-tools).
Otherwise, you can change the fonts in the source of `main.tex`, near the top.

Tools and packages used:

* LuaLaTeX.
* TikZ for graphics.
* Chris Monson's [Latex Makefile](https://github.com/shiblon/latex-makefile).
* XeLaTeX (to compile the datasheet in the `datasheet/` directory, if you wish to use it)

Inspired by Jesper Öqvist's thesis which can be found at https://github.com/llbit/joqvist-thesis

## Final dissertation as PDF

If you just want to see the dissertation in its final form, just open the file `linus_dissertation_final.pdf` in this repo, or [click here](https://linuskarlsson.se/papers/linus_dissertation_final.pdf) to view it from my personal web page.

## Compile dissertation from source

Run `make` from the root of this repository. Note that for successful compilation, you will need the fonts installed as described above.

To compile the datasheet, enter the `datasheet/` directory and run `xelatex datasheet.tex`
