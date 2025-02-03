#🃏/programming/python 

#####  What are the purpose of **\__init\__** and **\__new\__** methods? What are their usage cases? In what order and then are they invoked? Write an example of a custom **\__new\__** method in some class.
?
The **\__new\__** method creates an empty class instance, which is being later filled/configured with a help of  **\__init\__** method. So overriding the first method in my custom class can add some additional logic on the first stage, which is often used in [Singletone pattern](Design%20Patterns/Singletone%20pattern.md), or to apply different creation logic based on creation method (e.g. ***_from_file***,  ***_from_dict***).
Both methods are invoked automatically when you define a new class instance `instance = MyClass()`.
Custom **\__new\__** method example:
```python
class SomeClass:
	def __new__(cls, *args, **kwargs):
		# Any custom logic here
		instance = super().__new__(cls)
		print("I am born!")
		return instance
```
Notice! The **super()** method is used to call the parent class. As we have not defined our SomeClass to be someone's child explicitly, it is being a child of a general built-in Python **object** class.
`class SomeClass:` equals `class SomeClass(object):`
<!--SR:!2025-04-07,143,310-->

##### Imagine you have a custom class object:
```python
class Point:
	def __init__(self, x : int, y : int):
		self.x = x
		self.y = y

	def ???

mypoint = Point(1,2)
print(mypoint)
# Output: <Point object at .....>
```
What method should be implemented inside the class to achieve some custom output within the **print()** method like:
```python
print(mypoint)
# Output: Point(x=1,y=2)
```
?
You need to specify **\_\_str\_\_** or **\_\_repr\_\_** magic method inside your class. **print() prefers using the \_\_str\_\_** method, if you do implement both:
```python
def __repr__(self) -> str:
	return f"{type(self).__name__}(x={self.x}, y={self.y})"
```
<!--SR:!2025-07-08,235,330-->