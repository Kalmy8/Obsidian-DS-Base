[next \>](OOP%20Basics%20(2nd)%20lesson.md)
**Codewords:** OOP intuition, motivation behind it's usage

### The intuition behind OOP
OOP stands for **object-oriented programming**, and this paradigm shines when it comes to creating, managing, modifying some complex **objects**. To start applying this paradigm in first place, the most hardest part is detecting actual **objects** inside your programm. The truth is: Everything can be an object (actually, in Python, all built-in methods, data types and etc are **objects** themselves).

A typical object in OOP would have some **data** (attributes/properties/fields) and some **operations on it** (methods). 
Let's give you an intuition about OOP by using some real-world Analogies:

 Car:
 - **Properties:** `color`, `brand`, `model`, `fuel_level`
 - **Behaviors:** `refuel`, `re-paint`, `accelerate`

Take a few minutes and come up with some own real-world analogies, don't be afraid to list any objects, their properties and methods.

Note, that not all object have to really contain both properties and behaviors.

Some of them might only contain properties (so-called **dataclasses**)
Online shopping cart:
	- **Properties:** `volume`, `products`
	   - **Behaviors:** None

Some of them might only contain behaviors (so-called static classes)
Calculator (**static class**):
	- **Properties:** None
	- **Behaviors:** `add`, `subtract`, `multiply`

### Motivation behind OOP usage 
We are all used to some procedure programming from schools and universities, because it works well for some simple tasks which could fit in a single python script. More complex tasks usually do include usage of OOP pricniples, as it is actually **the most natural way to think**.

Whenever you are dealing with a new task, to actually DESCRIBE and write all the processes going. 

Example: 
Let's say you want to make a renovation in your new flat. What are the required steps to take? Let's write a recipe:
> In order to make the renovation, I firstly will hire a **supervisor: a man**, who will *find and communicate* proper specialists for me. First, he will hire a **measurer** *to make a complete measurement* and *pass all the data back to the supervisor*. When, a **designer** will *make a project of the flat*, with respect to all the measurements, and *return a list of the reqired furniture and it's parameters*. **Supervisor** *buys* all the furniture. Lastly, the **worker**  *places all the furniter to the corresponding positions*  .
```python
class Supervisor:
    def __init__(self):
        self.measurer = Measurer()
        self.designer = Designer()
        self.worker = Worker()
        self.measurements = None
        self.furniture_list = None

    def renovate(self):
        self.measurements = self.measurer.measure()
        self.furniture_list = self.designer.design(self.measurements)
        self.buy_furniture(self.furniture_list)
        self.worker.place_furniture(self.furniture_list)

    def buy_furniture(self, furniture_list):
        print("Supervisor: Buying furniture:")
        for item in furniture_list:
            print(f"  - {item}")

class Measurer:
    def measure(self):
        print("Measurer: Taking measurements...")
        measurements = {"length": 10, "width": 8, "height": 3}  # Example measurements
        print("Measurer: Measurements complete.")
        return measurements

class Designer:
    def design(self, measurements):
        print("Designer: Creating a design based on measurements...")
        furniture_list = []
        if measurements["length"] > 5:
            furniture_list.append("Large Sofa")
        else:
            furniture_list.append("Small Sofa")
        if measurements["width"] > 7:
            furniture_list.append("Large Table")
        else: 
            furniture_list.append("Small Table")
        print("Designer: Design complete. Furniture list created.")
        return furniture_list

class Worker:
    def place_furniture(self, furniture_list):
        print("Worker: Placing furniture:")
        for item in furniture_list:
            print(f"  - Placing {item}")
        print("Worker: Furniture placement complete")

# Create a Supervisor object and start the renovation
supervisor = Supervisor()
supervisor.renovate()
```


### From Analogy to Code 
1. **Classes and Objects (20 mins):**
   - **Class:** A blueprint or template for creating objects. (Like a car design).
   - **Object:** An instance of a class. (A specific car built from that design).
   - **Python Syntax:**
     ```python
     class Car:
       def __init__(self, color, brand, model):
           self.color = color 
           self.brand = brand
           self.model = model
           self.fuel_level = 0 

       def refuel(self, amount):
           self.fuel_level += amount

     my_car = Car('Red', 'Toyota', 'Camry') 
     print(my_car.color) # Accessing attributes
     my_car.refuel(50)   # Using methods
     ```
   - **Key Point:** Focus on the `self` parameter: It refers to the current object. 

####  Practical Tasks:
**Soda:** 
- Create a class to represent different types of soda. This class should accept one argument upon initialization to specify the flavor or additive
- Implement a method called **`show_my_drink()`** that prints a message indicating the type of soda.
- If an additive was specified, it should print "Soda with {ADDITIVE}". Otherwise, it should print "Regular soda".

**Bank Account:**
- Create a `BankAccount` class with attributes for `balance` and `account_number`. 
- Implement methods: `deposit()`, `withdraw()`, and `get_balance()`.  
- Encapsulate the balance so it cannot be directly modified outside the class.

**Simple Rectangle:**
- Create a `Rectangle` class with attributes `length` and `width`. 
- Implement methods to calculate the `area()` and `perimeter()`

**Library Book System:** 
- Begin designing a basic Library system:
- Have a `Book` class with attributes `title`, `author`
-  Create a `Member` class with attributes `First Name`, `Last Name` that can `borrow()` and `return_book()`
- Create a `Library` class that keeps track of:
	- Available books
	- Borrowed books
		- How long are they borrowed?
		- Which member did borrow the book?


#🃏/data-science 
## Key questions:

**What is the main idea behind Object-Oriented Programming (OOP)? **What are the two main components of an object in OOP? Provide a real world example
?
- OOP is a programming paradigm that structures code around "objects" which have data (attributes) and behaviors (methods)
- Example: A **Dog**:
	- **Behaviors:** bark, fetch, eat
	- **Properties:** breed, color, age
<!--SR:!2025-04-10,61,310-->


**In OOP, what is a class?**
?
A class is like a blueprint or template for creating objects.
<!--SR:!2025-04-04,55,310-->

**In OOP, what is an object?**. How could objects of the same class be different: can they have different methods? Can they have different attributes/attribute values?
?
- An object is a specific instance of a class.
- All objects do have the same methods
- Objects are likely to have different attribute values and can even have different attributes (**while not reccomended**)
<!--SR:!2025-04-14,65,310-->

**What does the `self` keyword represent in a Python class?**
?
It refers to the current instance of the class (the object itself).
<!--SR:!2025-04-11,62,310-->

**What is the purpose of the `__init__` method in a Python class?**
?
It's the constructor, used to initialize the attributes of an object when it's created.
<!--SR:!2025-04-06,57,310-->

**What is the difference between a "dataclass" and a "static class" as described in the conspect? Give a brief example of when you might use each one.**
?
 - **dataclass** primarily holds data, could not have any methods
	 - **Examples:** config files, vectors, points
 - **static class** mainly contains only the methods and doesn't have attributes
	 - **Examples:** a `MathUtils` class with methods like `add()`, `subtract()`, etc.
<!--SR:!2025-04-15,66,310-->


**Why is OOP often considered a more natural way to structure complex programs than procedural programming?**
?
OOP allows you to model real-world objects and their interactions more closely, making the code more organized and easier to understand.
<!--SR:!2025-04-09,60,310-->

**Programming Task:**
1. Write the Python code for the Dog class, including the **`__init__`**, **`bark()`** , and **`describe()`** methods.
2. Create at least two different Dog objects with different names and breeds.
3. Call the **`bark()`** and **`describe()`** methods on each of your Dog objects to test your implementation.
?
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def describe(self):
        print(f"This is {self.name}, a {self.breed}.")

# Create two Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Call methods on the objects
dog1.describe()  # Output: This is Buddy, a Golden Retriever.
dog2.describe()  # Output: This is Lucy, a Labrador.
```
<!--SR:!2025-04-03,54,310-->