[Python \_\_slots\_\_ and object layout explained - YouTube](https://www.youtube.com/watch?v=Iwf17zsDAnY)

Slots is a magic attribute written like 
```python
class Point:
	__slots__ = ('x', 'y')

	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y
```

Class instances defined with slots are a little bit different from the normal one:
- They have no `__dict__` attribute, because dictionary is not used for storing their attribute values
- They can have no any other attributes, despite one that are defined within the slots collection

This restrictions do result into great optimization benefits:
- Class instances consume 3+ times less memory
- Attributes take 20-30% less time to be accessed

The underlaying construction though is complex, so I won't write it down for now. Instead, you can just look it up an attached video.

One more thing to know is that with inheritance slotted attributes are also inherited from the base class. Children classes can define their own additional slot attributes:
```python
class Father:
	__slots__ = ('attr1', 'attr2')

class Child(Father):
	# additional slots: old one are also preserved
	__slots__ = ('additional_attr')
```

Notice, though, that multi-inheritance is not possible at all:
```python
class Father:
	__slots__ = ('father_attr')
	
class Mother:
	__slots__ = ('mother_attr')

class Child(Father, Mother):
	# Error
```


#🃏/job_questions 
## Key questions

What restrictions and benefits does the usage of `__slots__` class attribute provide?
?
- Restrictions:
	- Class instances can no more have any attributes not mentioned in `__slots__`
	- Class instances have no more `__dict__`, but rather `__slots__` attribute
- Benefits:
	- 20-30% increase of speed while accessing the attributes
	- 3+ times less memory consumption by the class instances
<!--SR:!2026-02-05,257,330-->


How do slots work with the simple inheritance and multi-inheritance?
?
- Simple inheritance: `__slots__` are automatically inherited from the parent object. Can provide additional attributes like
   `__slots__ = ('additional attribute')`
- Multi inheritance: is not possible, leads to an error
<!--SR:!2026-01-15,236,330-->
