# Packaging

A Python module is a <code>.py</code> containing Python definitions, statements, functions, and classes.
A package is a collection of Python modules into a directory with a ```__init__.py``` file.
A library is a collection of packages or it can be a single package.

- To create a package:
  1. create a folder with the package name.
  2. create an empty <code>__init__.py</code> file
  3. create the required modules
  4. in the <code>__init__.py</code> file, add code to reference the modules in the package
  
**example:**

```module1.py ```
```
def square(number):
    return number ** 2
```
```module2.py```
```
def doubler(number):
  return number * 2
```

```__init__.py```
```
from . import module1
from . import module2
```

your directory structure should look like this:
```
mypackage
mypackage/__init__.py
mypackage/module1.py
mypackage/module2.py
```

After creating the package, you can use it in other scripts if the package folder is in the same directory.
