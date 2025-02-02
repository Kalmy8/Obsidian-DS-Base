[\<previous](OOP%20Basics%20(2nd)%20lesson.md)  |  [next\>](OOP%20Basics%20(4th)%20lesson.md)
**Codewords:** OOP principles: **Inheritance and Polymorphism**

## Inheritance:

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

#### Practical Tasks:

**Task 1:** 
- Create a base class `Shape` with methods like `area()` and `perimeter()`. 
- Then, create subclasses like `Circle` and `Rectangle` that inherit from `Shape` and implement these methods specifically.

**Task 2:**
- Create a base class Vehicle with attributes like make, model, year, and color.
- Add a method display_info() that prints out the vehicle's information.
- Create subclasses Car and Motorcycle that inherit from Vehicle.
- Add specific attributes to each subclass (e.g., num_doors for Car, has_sidecar for Motorcycle).
- Override the display_info() method in the subclasses to also print the subclass-specific attributes.

**Task 3:**
- Create a base class Employee with attributes name and employee_id.
- Add a method calculate_pay() that returns 0 (as a placeholder, since pay calculation will be different for different types of employees).
- Create subclasses SalariedEmployee and HourlyEmployee.
- SalariedEmployee should have an attribute annual_salary. Override calculate_pay() to return the monthly salary (annual salary / 12).
- HourlyEmployee should have attributes hours_worked and hourly_rate. Override calculate_pay() to return the total pay (hours worked * hourly rate).

**Task 4:**
- Create a base class Media with attributes title and duration (in minutes).
- Add a method play() that prints "Playing [title]".
- Create subclasses Song and Movie that inherit from Media.
- Song should have an additional attribute artist. Override play() to print "Playing [title] by [artist]".
- Movie should have an attribute director. Override play() to print "Playing movie [title] directed by [director]".

## Polymorphism:

* **Definition:**  The ability of objects of different classes to respond to the same method call in their own way. It literally means "many forms." 
* **Illustration:** Consider the action "speak." A `Dog` object might respond with "Woof!", a `Cat` object with "Meow!", and a `Human` object with words.
    ```python 
    # Using the Dog and Cat classes from the Inheritance example:

    animals = [Dog("Max", 2, "Labrador"), Cat("Luna", 4, "Black")]

    for animal in animals:
        print(f"{animal.name} says:", end=" ")
        animal.speak()  
    ```

#### Practical Tasks:

**Task 1:**
- Create a base class Shape with an abstract method area() 
- Create subclasses Circle (with radius) and Rectangle (with length and width).
- Override the area() method in each subclass to calculate the area correctly.
- Create a list containing instances of both Circle and Rectangle.
- Use a loop to iterate through the list and call the area() method on each object, printing the result.

**Task 2:**
- Using the Animal, Dog, Cat hierarchy, create a list of different animal objects.
- Iterate through the list and call the speak() method on each animal, demonstrating polymorphism.

**Task 3:**
- Create a base abstract class PaymentMethod with an abstract method process_payment(amount) 
- Create subclasses CreditCard and PayPal that inherit from PaymentMethod.
- Override process_payment() in each subclass to print a message indicating how the payment is being processed (e.g., "Processing credit card payment of $..." or "Processing PayPal payment of $...").
- Create a list of different payment method objects.
- Iterate through the list and call process_payment() with a sample amount on each object.