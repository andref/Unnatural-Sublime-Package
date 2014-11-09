Natural Sublime Text Plugin
===========================

This is a Sublime Text plugin for [Software AG's Natural][natural], Cobol's ugly,
reatarded, babbling cousin. Made with ❤️ for those poor souls who — like me —
must endure the abhorrence on their day jobs.

May it inifinitesimally diminish your suffering.

[natural]: http://www.softwareag.com/corporate/products/adabas_natural/natural/overview


Features
--------

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
- Convert from natural-style to ugly-style data areas
- Autocomplete view names for `find`, `histogram` and `read`
- Autocomplete variable names when pressing . after a view name
- Autocomplete object names (in the same project) for `callnat`


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
