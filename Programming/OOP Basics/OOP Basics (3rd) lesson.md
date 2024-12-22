[[OOP Basics (2nd) lesson | <previous]]  |  [[OOP Basics (4th) lesson | next>]]
**Codewords:** OOP principles: **Inheritance and Polymorphism**

**3. Inheritance:**
* **Definition:** Creating new objects based on existing ones, inheriting their properties and behaviors.
* **Illustration:**  Imagine a base class "Animal" with properties like "name" and "age."  You can create subclasses like "Dog" and "Cat" that inherit these properties and add specific ones like "breed" for dogs or "fur_color" for cats.
    ```python
    class Animal:  
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def speak(self):
            print("Animal sound")

    class Dog(Animal):
        def __init__(self, name, age, breed):
            super().__init__(name, age)  
            self.breed = breed

        def speak(self): 
            print("Woof!")

    class Cat(Animal):
        def __init__(self, name, age, fur_color):
            super().__init__(name, age)
            self.fur_color = fur_color

        def speak(self):
            print("Meow!")

    pet1 = Dog("Buddy", 3, "Golden Retriever")
    pet2 = Cat("Whiskers", 5, "Gray")

    print(f"{pet1.name} is a {pet1.breed} and says:", end=" ")
    pet1.speak() 

    print(f"{pet2.name} has {pet2.fur_color} fur and says:", end=" ")
    pet2.speak()
    ```
* **Practical Task:**  Create a base class `Shape` with methods like `area()` and `perimeter()`. Then, create subclasses like `Circle` and `Rectangle` that inherit from `Shape` and implement these methods specifically.

**4. Polymorphism:**

* **Definition:**  The ability of objects of different classes to respond to the same method call in their own way. It literally means "many forms." 
* **Illustration:** Consider the action "speak." A `Dog` object might respond with "Woof!", a `Cat` object with "Meow!", and a `Human` object with words.
    ```python 
    # Using the Dog and Cat classes from the Inheritance example:

    animals = [Dog("Max", 2, "Labrador"), Cat("Luna", 4, "Black")]

    for animal in animals:
        print(f"{animal.name} says:", end=" ")
        animal.speak()  
    ```
* **Practical Task:** In your `Shape` example, demonstrate polymorphism by calling the `area()` method on objects of both the `Circle` and `Rectangle` classes. Observe how they calculate the area differently based on their specific shapes. 
