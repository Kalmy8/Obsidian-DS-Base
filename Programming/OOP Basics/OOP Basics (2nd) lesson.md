[[OOP Basics (1st) lesson | <previous]]  |  [[OOP Basics (3rd) lesson]]
**Codewords:** OOP principles: Encapsulation, Abstraction, Getters, Setters

## 1. Encapsulation:
*   **Definition:** Encapsulation is bundling data (variables) and the methods (functions) that operate on that data within a single unit—a class. **This protects the data by restricting direct access from outside the class and allows controlled access through defined methods.**
*   **Illustration:** Imagine a car. The engine, fuel tank, and braking system are all encapsulated within the car's body. You interact with the car through its controls (steering wheel, pedals) without directly manipulating the internal engine components.

    ```python
    class Car:
        def __init__(self):
            self.__fuel_level = 0  # Private variable (indicated by double underscore)

        def get_fuel_level(self):  # Getter method
            return self.__fuel_level

        def set_fuel_level(self, fuel_amount):  # Setter method
            if 0 <= fuel_amount <= 50:
                self.__fuel_level = fuel_amount
                print(f"Fuel level set to: {self.__fuel_level}L")
            else:
                print("Invalid fuel amount.")

        def fill_tank(self, fuel_amount):
            if 0 <= self.__fuel_level + fuel_amount <= 50:
                self.__fuel_level += fuel_amount
                print(f"Added {fuel_amount}L of fuel. Fuel level: {self.__fuel_level}L")
            else:
                print("Cannot overfill the tank.")

        def drive(self):
            if self.__fuel_level > 0:
                print("The car is moving.")
                self.__fuel_level -= 1
            else:
                print("The car is out of fuel.")

    my_car = Car()
    my_car.fill_tank(30)
    my_car.drive()
    print(f"Current fuel level: {my_car.get_fuel_level()}L")  
    
    # Accessing using getter
    my_car.set_fuel_level(45)  # Modifying using setter
    ```

- **Why Use Encapsulation?**
	-   **Data Protection:** Prevents accidental or unauthorized modification of data from outside the class
	-   **Flexibility:** Allows you to change the internal implementation of a class without affecting other parts of the code that use the class, as long as the interface (methods) remains the same.
	-   **Maintainability:**  Makes code easier to understand, debug, and maintain.

### Getters and Setters:
  - **Getters:** Methods that allow you to *retrieve* the value of a private attribute.
```python
def get_fuel_level(self):  # Getter method
            return self.__fuel_level
```
  - **Setters:** Methods that allow you to *modify* the value of a private attribute, often with validation to ensure data integrity.
```python
def set_fuel_level(self, fuel_amount):  # Setter method
            if 0 <= fuel_amount <= 50:
                self.__fuel_level = fuel_amount
                print(f"Fuel level set to: {self.__fuel_level}L")
            else:
                print("Invalid fuel amount."))
```

#### @property 
We should mention that Python has built-in instruments for creating getters and setters.

> I prefer not to use them, as it seems less obvious and clear for me. But knowing them is required to have no issues reading some other's code

```python
class MyClass:
    def __init__(self, value):
        self._value = value  # Using single underscore to indicate "protected"

    @property
    def value(self):  # Getter
        print("Getting value")
        return self._value

    @value.setter
    def value(self, new_value):  # Setter
        print(f"Setting value to {new_value}")
        if new_value > 0:
            self._value = new_value
        else:
            raise ValueError("Value must be positive")

    @value.deleter
    def value(self):  # Deleter
        print("Deleting value")
        del self._value

obj = MyClass(10)
print(obj.value)  # Accesses the getter: "Getting value" then "10"
obj.value = 20     # Calls the setter: "Setting value to 20"
# obj.value = -5  # Raises ValueError: Value must be positive
del obj.value      # Calls the deleter: "Deleting value"
```
**Explanation:**
1. **`@property`:**  The `@property` decorator above a method makes that method act like a "getter" for an attribute.
2. **`@<attribute>.setter`:** The `@<attribute>.setter` decorator above a method makes that method act like a "setter" for the attribute. The attribute name must match the name used with `@property`.
3. **`@<attribute>.deleter`:** The `@<attribute>.deleter` decorator defines a method to be called when the attribute is deleted (using `del`).





### Tasks

**Task 1**:
- Modify the `Car` class to include a private attribute `__mileage` (initial value 0) and a getter method `get_mileage()`. 
- Update the `drive()` method to increase `__mileage` each time the car is driven.

**Task 2:**
Create a `BankAccount` class. 
- Encapsulate the balance (`__balance`) as private. 
- Implement getter and setter methods `get_balance()` and `set_balance()` to access and modify the balance securely.
- Include validation in `set_balance()` to prevent negative balances. 
- Implement methods like `deposit()`, `withdraw()`.

## 2. Abstraction:
*   **Definition:** Abstraction focuses on showing essential information about an object while **hiding complex implementation details** from the user. It simplifies interaction with objects.
*   **Illustration:** Consider a coffee machine. You press a button for "espresso," but you don't need to know the exact internal process of grinding beans, heating water, or pressurizing the system.

    ```python
    class CoffeeMachine:
        def __init__(self):
            self.__water = 0  # Private attributes
            self.__beans = 0

        def fill_water(self, amount):
            self.__water += amount

        def fill_beans(self, amount):
            self.__beans += amount

        def make_espresso(self):
            if self.__water >= 30 and self.__beans >= 7:
                print("Making espresso...")
                self.__water -= 30
                self.__beans -= 7
                print("Enjoy your espresso!")
            else:
                print("Not enough water or beans.")

    machine = CoffeeMachine()
    machine.fill_water(100)
    machine.fill_beans(50)
    machine.make_espresso()
    ```
*   **Why Use Abstraction?**
    *   **Simplified Interface:** Users interact with objects through a clean, high-level interface.
    *   **Reduced Complexity:** Users don't need to understand the intricate inner workings.
    *   **Flexibility:** Internal implementation can be changed without affecting how users interact with the object.

### Tasks:
1. In the `CoffeeMachine` example, what are the essential actions a user needs to perform? What details are hidden from the user?
2. How does abstraction make the `CoffeeMachine` class easier to use?
3. Extend the `BankAccount` class: 
	- Introduce a method `calculate_interest()` that calculates the interest earned based on the current balance and a fixed interest rate. 
		- The user should not be able to see or modify the interest rate directly. Demonstrate how this exemplifies abstraction.


#🃏/data-science 
## Key questions

**What is encapsulation in OOP, and why is it important?**
?
Encapsulation is bundling data and methods within a class, protecting data integrity and controlling access through methods.
<!--SR:!2024-12-25,4,270-->

**What is the purpose of using "private" attributes (using the double underscore `__` prefix) in Python classes?**
?
To prevent direct access and modification of the attribute from outside the class, enforcing encapsulation.
<!--SR:!2024-12-25,4,270-->

**Why is direct access to an object's attributes generally discouraged in OOP?**
?
Direct access can lead to accidental or unauthorized modification of data, potentially corrupting the object's state or violating the intended logic of the class.
<!--SR:!2024-12-25,4,270-->

**Explain the purpose of "getter" and "setter" methods. Why are they important?**
?
**Getters** provide controlled access to read an object's attributes, while **setters** allow controlled modification, often including validation to ensure data integrity.
<!--SR:!2024-12-25,4,270-->

**Explain the concept of abstraction in OOP and provide a real-world example.**
?
- Abstraction hides complex implementation details and exposes only essential information to the user.
- Example: A TV remote control hides the internal electronics but provides buttons for essential actions like changing channels and volume.
<!--SR:!2024-12-25,4,270-->



