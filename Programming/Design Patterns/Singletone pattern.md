#🃏/design_patterns

What is a **Singletone** design pattern? When is it useful and how would you know if you will benefit from utilizng it? How does the **singletone** pattern utilizes **\__new\__** and  **\__init\__** methods in python? Provide some mock-code example of a class designed within a **singletone** paradigm.
?
Singletone is a [creational](Creational%20patterns.md) desing pattern forces the chosen class to have only one instance all over your application and to have one global entrypoint to that instance. This pattern is particularly useful when:
1. Your object operates with some shared resources, like the database connection. This is the most common use-case
2. You need one shared object and thruth-source across your application, let's say some sort of configuration class or logging class.
------------------------------------------------------------
Singletone design pattern example:
```python
class Singleton: 
	_instance = None 
	def __new__(cls, *args, **kwargs): 
		if cls._instance is None: 
			cls._instance = super().__new__(cls, *args, **kwargs) 
			return cls._instance 
			
	def __init__(self, value): 
	# Initialize instance variables only if it's the first time 
		if not hasattr(self, '_initialized'): 
			self.value = value 
			self._initialized = True
		# Ensure __init__ is not called again
```
Note: **\__init\__** method is called only once, when the first instance of Singleton class is created. However, there is an additional security step in this example, in case that **\__init\__** method is called manually.
<!--SR:!2025-09-22,64,310-->

## Practical tasks:
<!--SR:!2027-01-07,635,330-->

1. **App Config Manager**
    - Create a `ConfigManager` singleton that loads settings from a file once and provides read-only access globally.