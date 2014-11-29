Unnatural: Natural (Software AG) Sublime Text Package
=====================================================

This is a Sublime Text plugin for [Software AG Natural][natural], Cobol's
ugly, brain-damaged, BABBLING IN ALL-CAPS — but regrettably still healthy and
strong — cousin.

Made with ❤️ for those poor souls who — like me — must endure the abhorrence on
their day jobs. May it inifinitesimally diminish your suffering.

[natural]: http://www.softwareag.com/corporate/products/adabas_natural/natural/overview


Features
--------

### Version 0.2.0 — Oops

- Renamed to **Unnatural** because, really...
- Now compatible with ST2
- Line labels
- Understands all keywords — all 530 of them
- No more f... words printed on the console
- Consider the hyphen and hash sign as valid characters in an identifier

### Version 0.1.1

- Automatic indentation of control structures and subroutines
- Properly highlight unicode strings, date and time literals, and more keywords
  (but not all three million of them yet)
- Snippet for `decide on value` statement
- Automatically add a ruler to column 72, preserving other rulers the user may
  have defined
- Update variable levels when they are indented and unindented
- Key maps for Windows and Linux too

### Version 0.1.0

- Syntax highlighting (obviously)
- Snippets for `if`, `if-else`, `define subroutine`
- Comment toggling
- Symbol palette search for views and internal subroutines
- Autocomplete internal subroutine names for the `perform` statement
- Comment and uncomment empty lines


In the works
------------

- Autoindent variables when the level number is typed
- Language for data-definition
- Convert from natural-style to ugly-style data areas and back
- Autocomplete view names for `find`, `histogram` and `read`
- Autocomplete variable names when pressing . after a view, group or redefined
  name
- Autocomplete object names (in the same project) for `callnat`
- Handle "component based programing" 😏


License
-------

The MIT License (MIT)

Copyright (c) 2014 André Fillipe O. Silva <andre@filli.pe>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
