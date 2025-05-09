#🃏/oop-basics
What are the OOP principles? Enumerate them and highlight the key idea, 1-2 benefits they offer. Provide a code example as a demonstration.
?
**1. Encapsulation**
   - **Description:** Bundling data (attributes) and the methods (functions) that operate on that data within a single unit (the class).
   - **Key Idea:**  Hiding internal data and implementation details from the outside world. Access and modification of data should be controlled through well-defined methods (getters and setters).
   - **Benefits:**
     - **Data Protection:** Prevents accidental corruption of data.
     - **Flexibility:**  You can change internal implementation without affecting external code that uses the class.
   - **Example:**
 ```python
     class BankAccount:
         def __init__(self, balance=0):
             self._balance = balance  # Private attribute
<!--SR:!2026-02-20,287,330-->
             
         def deposit(self, amount):
             if amount > 0:
                 self._balance += amount
                 
         def withdraw(self, amount):
             if 0 < amount <= self._balance:
                 self._balance -= amount
                 
         def get_balance(self):
             return self._balance
```
The `_balance` attribute is private (convention in Python).
Access to the balance is controlled through methods (`deposit`, `withdraw`, `get_balance`).
**2. Abstraction**
   - **Description:** Simplifying complex systems by modeling them as objects with well-defined interfaces.
   - **Key Idea:**  Focusing on the essential features of an object and hiding irrelevant details from the user.
   - **Benefits:**
     - **Code Organization:**  Makes code easier to understand and manage.
     - **Reduced Complexity:**  Simplifies interactions with complex systems. 
   - **Example:**
```python
     class Car:
         def start(self):
             print("Engine started.") 
             
         def accelerate(self):
             print("Accelerating.")
             
         def brake(self):
             print("Braking.") 
```
The `Car` class provides a simplified abstraction of a real car.
Users don't need to know the internal complexities of the engine, transmission, etc. They interact through simple methods like `start`, `accelerate`, and `brake`.
**3. Inheritance**
   - **Description:**  Creating new classes (subclasses) that inherit properties and methods from existing classes (superclasses or base classes).
   - **Key Idea:**  Code reuse and establishing relationships between classes (is-a relationships). 
   - **Benefits:**
     - **Code Reusability:** Avoids code duplication by inheriting from existing classes.
     - **Extensibility:**  You can create specialized classes that extend the functionality of base classes.
   - **Example:**
 ```python
     class Animal: # Base class
         def __init__(self, name):
             self.name = name 
            
         def make_sound(self):
             print("Generic animal sound")
             
     class Dog(Animal): # Subclass
         def make_sound(self):
             print("Woof!")
             
     class Cat(Animal): # Subclass
         def make_sound(self):
             print("Meow!") 
 ```
`Dog` and `Cat` inherit from `Animal`.
 They override the `make_sound()` method to provide specific behavior.
**4. Polymorphism**
   - **Description:** The ability of objects of different classes to respond to the same method call in their own way.
   - **Key Idea:** "Many forms."  A single method call can have different behaviors depending on the type of object it's called on.
   - **Benefits:** 
      - **Flexibility:**  You can write code that works with different object types without needing to know their specific classes beforehand.
      - **Extensibility:**  You can add new object types without modifying existing code that uses polymorphic methods. 
   - **Example (Using the `Animal` classes from above):**
 ```python
 def animal_sounds(animal: Animal):
	 animal.make_sound()
	 
 dog = Dog("Buddy")
 cat = Cat("Whiskers")
 
 animal_sounds(dog) # Output: Woof!
 animal_sounds(cat) # Output: Meow! 
 ```
The `animal_sounds()` function can take any object of type `Animal` and will call the correct `make_sound()` method based on the object's actual type. 
**Remember:** These principles work together to create robust, flexible, and maintainable object-oriented code! 
<!--SR:!2024-12-08,4,270-->