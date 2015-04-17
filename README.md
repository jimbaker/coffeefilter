# CoffeeFilter

This is a starter project to play with writing Java servlet filters in
Python, using Jython and Clamp.

Start by installing Jython 2.7 from source, due
[this CLASSPATH bug](http://bugs.jython.org/issue2319) that's blocking
RC3, because it's rather annoying not to have `CLASSPATH` support for
doing this type of development. (The
[Jython dev guide](http://www.jython.org/devguide/) provides more
details.) You just want the developer build you get with just running
`ant`.

Make sure pip and setuptools are installed:

```bash
jython -m ensurepip`
```

then

```bash
pip install git+https://github.com/jythontools/clamp.git
```

(where pip is the one in the same bin directory as Jython!).

Next run

```bash
jython setup.py install singlejar
```

and this will produce a jar you can load as a ServletFilter, using the name `coffeefilter.CoffeeFilter`. Of course it will do nothing interesting just yet, since the code is as follows:

```python
class CoffeeFilter(ClampedBase, Filter):
    def init(self, filterConfig):
        raise NotImplementedError("implement!")

    def doFilter(self, request, response, chain):
        raise NotImplementedError("implement!")
        
    def destroy(self):
        raise NotImplementedError("implement!")
```
