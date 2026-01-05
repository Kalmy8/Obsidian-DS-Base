---
type: note
status: done
tags: ['tech/python']
sources:
-
- "[[Refactoring Guru - Design Patterns]]"
authors:
-
---
#🃏/semantic/design-patterns #🃏/refactoring-guru/design-patterns

What is a **Iterator pattern** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Iterator** paradigm.
?
[Iterator.mhtml](../../📁%20files/Iterator.mhtml)
The **Iterator pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to introduce a special **Iterator** object responsible for retrieving entities of some **collection** (a list, a tree, a dictionary and so on). Sometimes you have your complex data structure and is willing to iterate through it using some special strategy, with trees, for example, you can use depth-first or breadth-first strategies, or even return all elements in a random order. Moreover, you don't want to implement all of this strategies for each iterable object you have, so you should introduce some common iterable and iterator interfaces to **make multiple iteration strategies compatible with multiple data structures you have**.
##### Iterator pattern structure
![Pasted image 20240903124237.png](../../📁%20files/Pasted%20image%2020240903124237.png)
The pattern itself consists of **4 main parts**:
1. **Iterable interface (ABC):** a common interface for your iterables, declares one or multiple methods for getting iterators compatible with the collection `get_iterator(self)` .
2. **Iterator interface (ABC):** a common interface for your iterators,  declares the operations required for traversing a collection: fetching the next element, retrieving the current position, restarting iteration, etc.
3. **Concrete iterables:** a subclass of **Iterator \[2]**, which implements all the methods defined there using some concrete iteration logic/algorthim.
4. **Concrete iterators:** a subclass of **Iterable \[1]** which objects do implement all the collection methods, fields, functions, and do also implement some `get_iterator(self)` method.
> Note: Python offers you base **[Iterable and Iterator classes](../Iterable%20and%20Iterator%20classes.md)** avaliable from collections.abc library. These are compatible with default python instructions like `map(), reduce(), for,` etc.The complete usage of those is given below in the "Mock-code example" section.
##### Iterator Pattern usage scenarios
You can benefit from using the pattern in following situations:
---
1. Your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).
2. Use the pattern to reduce duplication of the traversal code across your app.
3. Use the Iterator when you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.
##### Command pattern mock-code example
```python
from collections.abc import Iterable, Iterator
from typing import Any

"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""

class AlphabeticalOrderIterator(Iterator):
 """
	Concrete Iterators implement various traversal algorithms.
	These classes store the current traversal position at all 
	times.
 """

 """
 `_position` attribute stores the current traversal position. 
 An iterator may have a lot of other fields for storing 
 iteration state, especially when it is supposed to work with 
 a particular kind of collection.
 """
 _position: int = None

 """
 This attribute indicates the traversal direction.
 """
 _reverse: bool = False

 def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
 self._collection = collection
 self._reverse = reverse
 self._position = -1 if reverse else 0

 def __next__(self) -> Any:
 """
 The __next__() method must return the next item in 
 the sequence. On reaching the end, and in subsequent 
 calls, it must raise StopIteration.
 """
 try:
 value = self._collection[self._position]
 self._position += -1 if self._reverse else 1
 except IndexError:
 raise StopIteration()

 return value

class WordsCollection(Iterable):
 """
 Concrete Collections provide one or several methods 
 for retrieving fresh iterator instances, compatible with 
 the collection class.
 """

 def __init__(self, collection: list[Any] | None = None) -> None:
 self._collection = collection or []

 def __getitem__(self, index: int) -> Any:
 return self._collection[index]

 def __iter__(self) -> AlphabeticalOrderIterator:
 """
 The __iter__() method returns the iterator object 
 itself, by default we return the iterator in 
 ascending order.
 """
 return AlphabeticalOrderIterator(self)

 def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
 return AlphabeticalOrderIterator(self, True)

 def add_item(self, item: Any) -> None:
 self._collection.append(item)

collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print(" ".join(collection)) 
# Output: First Second Third
print(" ".join(collection.get_reverse_iterator()), end="") 
# Output: Third Second First
```
<!--SR:!2026-08-06,484,310-->