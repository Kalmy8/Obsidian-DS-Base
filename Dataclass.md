---
type: note
status: done
tags: ['tech/python']
sources:
-
authors:
-
---

#🃏/semantic/python

What is the built-in @dataclass decorator from **dataclasses** library? How is it used, when is it being convinient? What other methods from the **dataclasses** library are often called alongside? What do they do?
?
The @dataclass decorator allows you to automatically constuct **\_\_init\_\_**, **\_\_repr\_\_**, **\_\_eq\_\_** methods within decorated class, which is very handy for classes which do only store and represent some data (that's why they are called dataclasses really).
```python
@dataclass 
class Student:
	name: str
	age: int
	marks: list = []

	# You can even define a post-init method which
	# will be called right after the hidden __init__ 
	def __post__init__(self):
		if self.age < 18:
			print('Родителей позови')
```
### Additional features:
1. **"Frozen" dataclasses:** works just like the normal ones, but become immutable after the creation, so all the fields are protected:
```python
@dataclass(frozen=True)
class ImmovablePoint
	x: int
	y: int
```
2. **field** object from dataclasses library:
	- **Setting Default Values**: You can provide a `default` argument to `field()` to specify a default value for a field. This is similar to setting default values in a regular class's `__init__` method.
	- **Using Default Factory Functions:** For mutable data types like lists or dictionaries, you should use a `default_factory` function. This ensures that each instance of the dataclass gets its own independent list or dictionary.
	- **Making Fields Non-Comparable:** By setting `compare=False`, you can exclude a field from comparisons (`__eq__` method) of dataclass instances. This is useful for fields that don't contribute to the object's equality logic.
	- **Representing Fields in the `repr()` Output:** `repr=False` hides a field from the string representation (`__repr__`) of the dataclass.
	- **Initializing Fields with Metadata:** The `metadata` argument allows you to attach arbitrary metadata to a field. This can be useful for documentation, validation, or other custom logic.
```python
from dataclasses import dataclass, field

@dataclass
class MultiFieldExample:
 # Default value
 name: str = field(default="Default Name")

 # Default factory function
 items: list = field(default_factory=list)

 # Non-comparable field
 metadata: dict = field(default_factory=dict, compare=False)

 # Excluded from repr
 password: str = field(repr=False, default="secret")

 # With metadata
 description: str = field(
 default="A default description", 
 metadata={'doc': 'This is the description of the object.'}
 )

# Usage Example
example = MultiFieldExample()
print(example)
# Output: MultiFieldExample(name='Default Name', items=[], metadata={}, description='A default description')

example.items.append("Item 1")
print(example.items) # Output: ['Item 1']

print(example.password) # Output: secret 
# But 'password' is not included in the repr output above
```
3. **Asdict and astuple** methods do represent a dataclass as a dictionary and as a tuple accordingly:
```python
from dataclasses import asdict, astuple

person = Person(name="Alice", age=30)
print(asdict(person)) # {'name': 'Alice', 'age': 30}
print(astuple(person)) # ('Alice', 30)
```
4. **Replace** method creates a copy of a dataclass but allow you to change some fields within:
```python
from dataclasses import replace

new_person = replace(person, age=31)
print(new_person) # Output: Person(name = 'Alice', age = 31)
```
<!--SR:!2026-04-26,427,310-->