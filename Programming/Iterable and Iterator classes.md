#🃏/programming/python
#🌱
What are the **Iterable and Iterator** python built-in classes? What methods should they implement and what are their usage?
?
Both classes can be used to created some data collections avaliable for traversing (iterating) through. Let's observe and describe them:
###### **Iterator**
is the class responsible for iteration process over some collection, which is being passed during iterator initialization. To perform the iteration process, it has to implement a few required methods:
1. **`__iter__(self)` method:** returns an **Iterator** itself (so the body of the method is just `return self`). While seeming meaningless, that is necessary for some python iterator usage scenarios such as "for" loops. That also allows you to work directly with iterator objects using **sorted(iterator)**, **list(iterator)** and so on.
2. **`__next__(self)` method:** returns the next object in the bounded collectio and **raises StopIteration** error at the end.
```python
class MyIterator: 
	def __init__(self, data): 
		self.data = data self.index = 0 
		
	def __iter__(self): 
		return self 
		
	def __next__(self): 
		if self.index < len(self.data): 
			result = self.data[self.index] 
			self.index += 1 
			return result 
		else: raise StopIteration
```
###### **Iterable**
is the class avaliable for some basic travesing and it should implement just one required **`__iter__()` method**. This method **should create and return an iterator object, which can handle the iteration process through that collection**. If an object is iterable, it can be used in a `for` loop, in list comprehensions, or with functions like `map()`, `filter()`, and `sorted()`. There might be some other methods, commonly defined ones are:
	- **`__len__()`**: This method returns the number of items in the iterable. It allows you to use the `len()` function on the iterable.
	- **`__getitem__(index)`**: This method retrieves an item from the iterable by index. It allows the iterable to support indexing and slicing.
	- **`__contains__(item)`**: This method checks whether a specific item is present in the iterable. It allows the use of the `in` keyword.
	- **`__reversed__()`**: This method returns an iterator that accesses the iterable's items in reverse order.
	- **`__str__()` and `__repr__()`**: These methods are used to represent console via `print(), repr(), str()` methods. Note that the **print() prefers using the `__str__()` method if you implement both**.
```python
class MyIterable(Iterable): 
	def __init__(self, data): 
		self._data = data 
		
	def __iter__(self): 
		return MyIterator(self._data) 
		
	def __len__(self): 
		return len(self._data) 
		
	def __getitem__(self, index): 
		return self._data[index] 
		
	def __contains__(self, item): 
		return item in self._data
```


**ITERATOR** - a Python **object** with a special **`__next__()`** method, enabling iteration through a sequence.

**ITERABLE** - a Python **object** with either a **`__iter__()`** method (returning an **ITERATOR**) or a **`__getitem__()`** method. Basic Python iterables are **lists, sets, tuples, dictionaries, ranges, str**.  The use of **`__getitem__`** for iteration is primarily for backward compatibility with older code or specialized cases. If an object has **`__getitem__`** but no **`__iter__`**, Python will attempt to create a default iterator that accesses elements sequentially by index using **` __getitem__`**. However, this is not the preferred or recommended approach for new code.