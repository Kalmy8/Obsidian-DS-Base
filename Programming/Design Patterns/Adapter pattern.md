---
type: note
status: done
tags: ['tech/python']
sources:
- "[[Refactoring Guru - Design Patterns]]"
authors:
-
---
#🃏/semantic/design-patterns #🃏/refactoring-guru/design-patterns

What is an **Adapter** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Adapter** paradigm.
?
An **Adapter** design pattern allows you to make incompatible interfaces works together. Imagine you are going to visit the USA, riding from Europe, and take your power socket with you. You won't be able to plug it into an American nest, because they are incompatible, so you have to buy **an adapter**. Just like that, you can adapt one class to work with the desired interface.
The **adapter** pattern itself contains **3 main parts**:
1. **A target interface**, that is the desired interface you wish you could work with (e.g. an American nest).
2. **An adaptee**, an object that doesn't meet the desired target interface, though it contains some useful functionality.
3. **An adapter**, an object created to make the **adaptee** meet the **target interface**.
<br>
It is useful when:
1. You are importing some libraries with the desired functionality, but their classes interface doesn't meet your application common interface.
2. You want to re-use some existing code, but have to add some small modifications to it, to adapt it for a new task.
3. You are working on a legacy project, and have to refresh and re-use some small classes and methods with the new interface, or vice versa.
------------------------------------------------------------
Adapter design pattern example:
```python

class AmericanSocket:
	def connect(self):
		pass

class EuropeanSocket:
	def plug_in(self):
		pass

class European2AmericanAdapter(AmericanSocket):
	def __init__(european_socket: EuropeanSocket):
		self.european_socket = european_socket 
	
	def connect(self):
		print("Adapter: Converting to American socket.")
		self.european_socket.plug_in()
```
<!--SR:!2026-12-18,618,330-->
