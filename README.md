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
