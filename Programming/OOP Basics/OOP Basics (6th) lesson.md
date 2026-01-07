---
type: note
status: done
tags: ['tech/python']
sources:
-
- "[[OOP Basics Course]]"
authors:
-
---

[[TODO OOP Basics (5th) lesson|< previous]]
**Codewords:** Magic Methods (Descriptors)

## Introduction
Magic methods (dunder methods) allow objects to interact with Python's built-in operations. They're essential for creating intuitive class behaviors.

## `__call__(self, ...)`
Allows instances to be called like functions.

```python
class Multiplier:
 def __init__(self, factor):
---
 self.factor = factor

 def __call__(self, x):
 return self.factor * x

double = Multiplier(2)
print(double(5)) # Output: 10
```

##### Practice Problems:

- Create an `Exponent` class that raises numbers to a given power when being called
```python
class Exponent:
 def __init__(self, power):
 self.power = power

 def __call__(self, x):
 return x ** self.power

square = Exponent(2)
print(square(4)) # Should output 16
```

## String Representation: `__repr__` vs `__str__`

- `__repr__`: Unambiguous representation for developers. Is used by python when `__str__` is not defined.
- `__str__`: Readable format for end-users

```python

class Coordinate:
	def __init__(self, x, y):
 self.x = x
 self.y = y

 def __repr__(self):
 return f"Coordinate({self.x}, {self.y})"

 def __str__(self):
 return f"({self.x}, {self.y})"

coord = Coordinate(3, 4)
print(repr(coord)) # Coordinate(3, 4)
print(str(coord)) # (3, 4)
```

##### Practice Problem:

- Create a **`Book`** class, accepting `title` and `author` parameters in the initializer, and implement `__repr__` or `__str__` descriptor to print the book object nicely

```python
class Book:
 def __init__(self, title, author):
 self.title = title
 self.author = author

 def __repr__(self):
 return f"Book({self.title!r}, {self.author!r})"

 def __str__(self):
 return f"'{self.title}' by {self.author}"
```

## Hashing and Equality: 

- **Hash** is a unique static identificator, representing the object
	- `__hash__` is a method, which should return object's hash
-  `__eq__` is method used by comparison operator ( `= =)`, logically saying that two objects are identical (even if their `id()` is different) or not 
	- If two objects are identical `one = = two`, then their hashes should be identical `hash(one) = = hash(two)`
- Implementing both `__hash__` and `__eq__` descriptors is essential for objects usage inside sets/dicts
- Mutable objects should not have `__hash__` descriptor, unless their equality does not rely on included elements (so `container1 = =  container2` even if container's elements are different)
	- Thus mutable objects can not be used as dictionary keys, overwise `unhashable type` error appears
```python
class Student:
 def __init__(self, id, name):
 self.id = id
 self.name = name

 def __eq__(self, other):
 return isinstance(other, Student) and self.id == other.id

	# hash should rely on the same attribute as __eq__
 def __hash__(self):
 return hash(self.id)

student1 = Student(123, "Alice")
student2 = Student(123, "Alicia")
print(student1 == student2) # True
students = {student1, student2}
print(len(students)) # 1
```

##### Practice Problems:

- Code `User` class, which takes `email` and `name` parameter in it's intializer
- Implement equality and hashing such that:
 - Users are considered equal if emails match CASE-INSENSITIVELY
 - Hash should be based on lowercased email

```python
class User:
 def __init__(self, email, name):
 self.email = email
 self.name = name
 
 def __eq__(self, other):
 return (isinstance(other, User) and 
 self.email.lower() == other.email.lower())
 
 def __hash__(self):
 return hash(self.email.lower())

# Test case
user1 = User("ALICE@example.com", "Alice")
user2 = User("alice@example.com", "Alicia")
print(user1 == user2) # Should be True
```

- Code `Configuration` mutable class, which takes a list in it's intializer and makes a deepcopy of that list
- Define the `update` method, which will take a `key` and a `value` as it's parameters, and update the underlying class accordingly
- Implement `__eq__` method so same configurations will be assumed equal
- DO NOT implement`__hash__` method
	- Try to add `Configuration` class instance inside a python set, check that you are getting an error

```python
class Configuration:
 def __init__(self, values):
 self.values = values.copy()

 def update(self, key, value):
 self.values[key] = value
 
 def __eq__(self, other):
 return (isinstance(other, Configuration) and 
 self.values == other.values)
 
 # No __hash__ implementation (inherits object's __hash__)

# Test case
config1 = Configuration({"theme": "dark"})
config2 = Configuration({"theme": "dark"})
print(config1 == config2) # Should be True
try:
 {config1: "test"}
except TypeError as e:
 print(e) # Should raise unhashable type error
```

## Comparison Operators

- Implement comparison (`>, >=, <, <=, ==, ...)` logic for custom objects
- which is also useful when using `sort()` function
- If some operators are missing, python will raise a corresponding error if you'll try to compare elements using that operator
- You could define only `__eq__` and `__le__` comparison operator, and python will auto-complete all the others if you use `from functools import total_ordering`

```python
class Temperature:
 def __init__(self, celsius):
 self.celsius = celsius

 def __lt__(self, other):
 return self.celsius < other.celsius

 def __le__(self, other):
 return self.celsius <= other.celsius

 # Similar for __gt__, __ge__
 
t1 = Temperature(25)
t2 = Temperature(30)
print(t1 < t2) # True
```

##### Practice Problem:

- Code a `PlayingCard` class, taking the rank ('6', '7',...,'A') in it's initializer. The class should implement comparison methods with respect to real card-game logic ('A' > 'K' > 'Q' > ... > '6') 
```python
class PlayingCard:
 RANKS = {'2':2, '3':3, ..., 'A':14}
 
 def __init__(self, rank, suit):
 self.rank = rank
 self.suit = suit

 def __lt__(self, other):
 return self.RANKS[self.rank] < self.RANKS[other.rank]
```

## Container Emulation Methods

- Allow custom objects mimic built-in containers behaviour (`len()` usage, `in` operator usage, `container[index]` element access..)
- To allow for object iteration (using `for x in my object`), `__getitem__` method should be implemented
	- It's generally not reccomended to do so, `__iter__` method should be defined instead (refer to [[Iterable and Iterator classes | this conspect]])

```python
class Playlist:
 def __init__(self, songs):
 self.songs = list(songs)

 def __len__(self):
 return len(self.songs)

 def __getitem__(self, index):
 return self.songs[index]

	def __setitem__(self, index, value):
		self.songs[index] = value

 def __contains__(self, song):
 return song in self.songs

my_playlist = Playlist(['Song1', 'Song2'])
print(len(my_playlist)) # 2
print('Song1' in my_playlist) # True
```

##### Practice Problem:

- Code `SmartDictionary` class, which initializer won't take any parameters, but will initialize an empty dictionary
- Override `__getitem__` and `__setitem__` methods so your dictionary will become **case-insensitive**, check that `mydictionary[City] is mydictionary[CITY]` **is True**
```python
class SmartDictionary:
 def __init__(self):
 self.data = {}

 def __setitem__(self, key, value):
 self.data[key.lower()] = value

 def __getitem__(self, key):
 return self.data[key.lower()]

d = SmartDictionary()
d['City'] = 'Paris'
print(d['CITY']) # Should output 'Paris'
```

#🃏/semantic/oop #🃏/source/oop-basics-course 
## Key questions

How to make a class callable (act as a function)?
?
- Implement `__call__` method
<!--SR:!2026-01-09,4,270-->

What's the difference between `__str__` and `__repr__`?
?
- `__str__` is user-friendly,
- `__repr__` is unambiguous usually shows how to recreate the object, and is used as a fallback if `__str__` is not implemented
<!--SR:!2026-01-09,4,270-->

What methods are needed to use objects in a `set` or a `dict`?
?
- Both `__hash__` and `__eq__` methods
<!--SR:!2026-01-09,4,270-->

What is the relationship between `__eq__` and `__hash__` methods? Why should they rely on same attributes?
?
- If two objects are equal, they should have the same hash
- That actually explains why they should rely on same logic: if attribute has changed, both `__eq__` and `__hash__` should change (or not change) to remain in sync
<!--SR:!2026-01-09,4,270-->

Several questions about writing custom python containers:
- How to enable `for item in my_object` syntax?
- How would you make `obj[key] = value` work?
- How would you make `len(obj)` work?
- How would you make `x in obj` work?
?
- Implement `__getitem__` method (it's better to implement `__iter__` actually, read [[Iterable and Iterator classes | here]])
- Implement `__setitem__` method
- Implement `__len__` method
- Implement `__contains__` or `__iter__` + `__getitem__`
<!--SR:!2026-01-09,4,270-->

