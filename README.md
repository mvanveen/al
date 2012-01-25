Al - Automatic Alias Setter
---------------------------

I never set aliases for myself, even though I know they're convenient.  This
largely a result of not having a persistent `alias` command in the shell, as
I am too lazy to edit my `/.zshrc` by hand..

### Work In Progress

`al` is a work in progress.  I don't think it needs to be much more than what 
is already, but I do have plans to extend it.

I plan to support a number of different shells and want to make the public
interface so beautiful that @kennethreitz would smile tears of well-documented
joy if he saw it.

That's likely a ways away, but v1 is sufficient for my personal use right now. 

Hopefully you find it useful too!

Installation
------------

Just set the `PATH` variable in `al.py` to where your rc file is and you should 
be good to go.

Usage
-----

1. Alias `cat` to `c`

```
    $ python al.py c cat
```

2. Multi-word alias

```
    $ python al.py gs "git status --short"
```
2. Meta-al

```
    $ python al.py al /path/to/all.py
```

License
-------

Al is MIT licensed.

    Copyright (C) 2012 Michael Van Veen

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
