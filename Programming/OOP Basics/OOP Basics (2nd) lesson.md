[[OOP Basics (1st) lesson | <previous]]  |  [[OOP Basics (3rd) lesson | next>]]
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
- Implement methods like `deposit()`, `withdraw()`

**Task 3:** 
Create a `Triangle` class initialized from a given set of side lengths. 
- The class should take a list of strictly positive numbers as input. Otherwise errors do appear:
	- **"Negative numbers cannot be used!"**
	- **"Only numbers can be used!"**
- You should also check if triangle can be formed with this given lengths. Otherwise an error appears:
	- **"Unfortunately, a triangle cannot be formed from these sides."**


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
**Task 1:**
- In the `CoffeeMachine` example, what are the essential actions a user needs to perform? What details are hidden from the user?
- How does abstraction make the `CoffeeMachine` class easier to use?

**Task 2:**
- Extend the BankAccount class (from the Encapsulation section).
- Add a private attribute __interest_rate (e.g., set it to 0.05 for 5%).
- Introduce a method calculate_interest() that calculates the interest earned based on the current balance and the __interest_rate.
- Add a method apply_interest() that adds the calculated interest to the balance.
- Explain how these additions demonstrate abstraction.

**Task 3:**
1. **Create a TV class:**
    - Include private attributes for __is_on (boolean, initially False), __volume (integer, initially 10), and __channel (integer, initially 1).
    - Implement private methods:
        - _change_volume(amount): Increases or decreases the volume by amount, ensuring it stays within the range 0-100.
        - _change_channel(channel): Changes the channel to the given channel number (assume a valid range of 1-100).
    - Implement public methods:
        - power_on(): Turns the TV on.
        - power_off(): Turns the TV off.
        - volume_up(): Increases the volume by 1 if the TV is on.
        - volume_down(): Decreases the volume by 1 if the TV is on.
        - channel_up(): Goes to the next channel if the TV is on.
        - channel_down(): Goes to the previous channel if the TV is on.
2. **Create a RemoteControl class:**
    - The constructor (__init__) should take a TV object as an argument and store it as an attribute.
    - Implement methods power_on(), power_off(), volume_up(), volume_down(), channel_up(), and channel_down() that correspond to the TV's methods. These methods should simply call the appropriate methods on the TV object.
3. **Demonstrate Abstraction:**
    - Create a TV object.
    - Create a RemoteControl object associated with the TV.
    - Use the RemoteControl to turn the TV on, adjust the volume and channel, and then turn the TV off.
    - Explain how this example demonstrates abstraction.


**Task 4:**
1. **Create an Order class:**
    - Include an attribute items (a list to store items in the order).
    - Implement a method add_item(item_name, price, quantity) to add an item to the order.
    - Implement a method get_total() that calculates and returns the total price of the order.
        
2. **Create a PaymentProcessor class:**
    - Implement a method charge_payment(order, payment_method) that simulates charging a payment.
    - For now, it can simply print a message like "Processing [payment_method] payment of $[amount]..." (where [amount] is the order total).
3. **Create an InventoryManager class:**
    - Implement a method check_stock(order) that simulates checking if items in the order are in stock.
        - For simplicity, you can assume all items are in stock, or you can add a simple check (e.g., if an item name is "out_of_stock_item", return False).
    - Implement a method update_stock(order) that simulates updating the stock after an order is processed (e.g., print a message).
4. **Create a ShippingManager class:**
    - Implement a method ship_order(order) that simulates shipping the order (e.g., print a message).
5. **Create an OrderProcessor class:**
    - The constructor should create instances of PaymentProcessor, InventoryManager, and ShippingManager.
    - Implement a method process_order(order, payment_method) that does the following:
        - Checks inventory using InventoryManager.check_stock().
        - If sufficient stock:
            - Charges payment using PaymentProcessor.charge_payment().
            - Updates stock using InventoryManager.update_stock().
            - Ships the order using ShippingManager.ship_order().
            - Prints a success message.
        - If insufficient stock:
            - Prints an appropriate message.
6. **Demonstrate Abstraction:**
    - Create an Order object and add some items to it.
    - Create an OrderProcessor object.
    - Call the process_order() method on the OrderProcessor object to process the order.
    - Explain how this example demonstrates abstraction (what details are hidden from the user of the OrderProcessor?).

#🃏/data-science 
## Key questions

**What is encapsulation in OOP, and why is it important?**
?
Encapsulation is bundling data and methods within a class, protecting data integrity and controlling access through methods.
<!--SR:!2025-02-01,14,290-->

**What is the purpose of using "private" attributes (using the double underscore `__` prefix) in Python classes?**
?
To prevent direct access and modification of the attribute from outside the class, enforcing encapsulation.
<!--SR:!2025-02-03,16,290-->

**Why is direct access to an object's attributes generally discouraged in OOP?**
?
Direct access can lead to accidental or unauthorized modification of data, potentially corrupting the object's state or violating the intended logic of the class.
<!--SR:!2025-02-02,15,290-->

**Explain the purpose of "getter" and "setter" methods. Why are they important?**
?
**Getters** provide controlled access to read an object's attributes, while **setters** allow controlled modification, often including validation to ensure data integrity.
<!--SR:!2025-02-01,14,290-->

**Explain the concept of abstraction in OOP and provide a real-world example.**
?
- Abstraction hides complex implementation details and exposes only essential information to the user.
- Example: A TV remote control hides the internal electronics but provides buttons for essential actions like changing channels and volume.
<!--SR:!2025-02-03,16,290-->

**Task:**
- Create a class Circle with a private attribute radius. 
- Implement a getter method get_radius() and a setter method set_radius() that validates if the radius is positive.
?
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive.")

# Example usage
my_circle = Circle(5)
print(my_circle.get_radius())  # Output: 5
my_circle.set_radius(10)
print(my_circle.get_radius())  # Output: 10
my_circle.set_radius(-2)      # Output: Radius must be positive.
```
<!--SR:!2025-02-15,30,310-->

**Task:**
- Create a class Playlist with methods add_song(song_title), remove_song(song_title), and play().
- Internally, you can store the songs in a list (this is a hidden detail).
- The play() method should simply print "Playing [song_title]" for each song in the playlist.
?
```python
class Playlist:
    def __init__(self):
        self.__songs = []  # Private attribute to store songs

    def add_song(self, song_title):
        self.__songs.append(song_title)
        print(f"Added '{song_title}' to the playlist.")

    def remove_song(self, song_title):
        if song_title in self.__songs:
            self.__songs.remove(song_title)
            print(f"Removed '{song_title}' from the playlist.")
        else:
            print(f"'{song_title}' not found in the playlist.")

    def play(self):
        if self.__songs:
            print("Playing playlist:")
            for song in self.__songs:
                print(f"- Playing {song}")
        else:
            print("Playlist is empty.")

# Example Usage:
my_playlist = Playlist()
my_playlist.add_song("Song A")
my_playlist.add_song("Song B")
my_playlist.add_song("Song C")
my_playlist.play()
my_playlist.remove_song("Song B")
my_playlist.play()
```
<!--SR:!2025-02-15,30,310-->