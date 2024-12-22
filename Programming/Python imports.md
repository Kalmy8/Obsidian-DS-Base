*original article: [The definitive guide to Python import statements - Zean Qin](https://zean.be/articles/definitive-guide-python-imports/#absolute-vs-relative-import)*

---
Let's begin with some basic commonly-used definitions:
1. **Python package:** any folder containing .py files, commonly will also include an *\_\_init\_\_.py* file.
2. **Python module:** any .py script.
3. **Python built-in module:** a module written in C (for CPython) and integrated right into interpretator.
4. **Python object:** every entity in Python is an object: a function, a variable, a class, a generator object...

Python `import` statement can be used within one of your **modules**, and it immideately do 2 things:
1) Executes all the code within that module
2) Makes specifed/all the objects (functions, variables) within that module accessible

> Note: there are several ways to use `import`
>	- import \<module>
>	- import \<package>
>	- from \<package> import \<module or subpackage or object>
>	- from \<module> import \<object>
>	- import X as Y (this one renames any imported object)
> You can choose any option, the 2 steps declined above will work anyway

### Basics of the Python `import` and `sys.path`
When the module is imported, the interpreter searches for it's name in the following sequence:
1. Firstly, he tries to find the built-in module with such a name (like math, itertools, sys, time...). All such modules are listed inside `sys.builtin_module_names` variable. 
> Note: some modules (like `random` are the part of the Python standart distribution package, but they are not built-ins cause they are not inserted inside the Python Interpreter itself).
2. Secondly, he tries to find this name inside the `sys.path` variable. `sys.path` variable, on it's own, is initialized from several sources, and will import the requested module **from the first found source**:
	  1. the directory containing the input script (or the current directory, if you are in an interactive python session)
	  2. PYTHONPATH
	  3. Installation-dependent default (global site packages and virtual environment directories) 

> Note: importing from the  **from the first found source** means that you can override some modules, which seems very strange. The `random` module, for example, is an *Installation-dependent default \[3]*, so if you will create your own `random` module inside the *script directory \[1]* it will be imported instead.

**`sys.path` variable is being shared across all imported modules**, so if you some module inside the project root, each script within the project subfolders will be able to import each other since the project root is presented on the syspath. And vice-versa: if you launch your module directly, it won't be able to access any modules laying above (in the parent directories), unless you implement some workaround (explicitly modyfing the sys.path variable, for example).

### \_\_init\_\_.py role
The first time that a package or one of its modules is imported, Python will execute the `__init__.py` file in the root folder of the package if the file exists. All objects and functions defined in `__init__.py` are considered part of the package namespace.

importing \<package> is the just the same thing as importing <\_\_init\_\_.py> module of that package

### Relative imports
A **relative import** uses the relative path (starting from the path of the current module) to the desired module to import.  It follows the format `from .<module/package> import X`, where `<module/package>` is prefixed by dots `.` that indicate how many directories upwards to traverse. A single dot `.` corresponds to the current directory; two dots `..` indicate one folder up; etc.

> Note: be aware that using dots can lift you up no higher than the sys.path subfolders. 

### Common problems
It's easy to maintain a project which is always launched by a script from the project root directory, as the project root will appear on a sys.path making all possible absolute and relative imports possible

**Problems occure when you are trying to build flexible modules which could be runned both by themselves or be imported**.

Let's say your project structure looks like this:
```
my_project/
├── package_a/
│   ├── __init__.py
│   ├── utils.py
	├── subpackage_b/
		├── module_x.py
└── my_script.py 
```
your `my_script.py` file contains such an import:
`from package_a.subpackage_b import module_x.py`

and your `module_x.py` file contains such an import:
`from package_a import utils`

What will happen if you try to launch `module_x.py` directly or import to the  `my_script.py`?
	1.  If you do launch `my_script.py`, then the whole `my_project/` folder will be added to the `sys.path`, meaning that python interpreter will be able to resolve any package names that you mention. So `my_script.py` will successfully import  `module_x.py`, which will successfully import  `utils.py` on it's own.
	2.  If you do launch `module_x.py` directly, when only the `subpackage_b/` folder will be added to `sys.path`, and the interpreter won't be able to import any scripts from the parent directories, so the `from package_a import utils` line will fail with an error.

There are some workaround #TODO

### Miscellaneous 
- use  `__all__` variable in `__init__.py` for specifying what gets imported by `from <module> import *`
- use `if __name__ == '__main__'` to check if a script is imported or runned directly.
- install a project as a package (in developer mode) with `pip install -e <project>` to add the project root directory to `sys.path`
- Know that \`from <module> import *` does not import names from `<module>` that begin with an underscore `_`