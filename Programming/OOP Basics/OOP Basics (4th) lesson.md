[\<previous](OOP%20Basics%20(3rd)%20lesson.md)  |  [[OOP Basics (5th) lesson | next >]]
**Codewords:** SOlid principles

**Theory:** [SOLID principles](../SOLID%20principles.md)
**Practice:**

For each code snippet:

1. **Identify the Smell:** Carefully examine the code and identify the specific parts that violate the SOLID principle in question.
2. **Explain the Problem:** Describe *why* the code violates the principle and what problems this violation might cause.
3. **Refactor:** Rewrite the code to address the identified issues and make it adhere to the SOLID principle.


### S - Single Responsibility Principle (SRP)

**Definition:** A class should have only one specific reason to change

**Task 1:**
```python
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        
    def change_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
        else:
            print("Invalid email format.")
            
    def save_to_database(self):
        # Code to connect to database and save user data...
        print(f"Saving {self.name}'s data to database...")
```

> [!note]- Identify the Smell
>  The `User` class has multiple responsibilities: managing user data (`name`, `email`, `address`) and handling database operations (`save_to_database`).

> [!note]- Explain the Problem
>If the database logic changes (e.g., switching to a different database or changing the table structure), you'll have to modify the `User` class. Also, if the user data handling logic changes, you might need to change database-related code. This violates SRP, making the class harder to maintain and prone to errors.

>[!note]- Refactor
> Separate the database logic into a different class.
```python
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def change_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
        else:
            print("Invalid email format.")

class UserDatabase:
    def save(self, user):
        print(f"Saving {user.name}'s data to database...")

# Example usage
user = User("Alice", "alice@email.com", "123 Main St")
db = UserDatabase()
db.save(user)
```

**Task 2:**

```python
class Order:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def calculate_total(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i]
        return total

    def print_order(self):
        for i in range(len(self.items)):
            print(f"{self.items[i]}: ${self.prices[i]}")
        print(f"Total: ${self.calculate_total()}")

    def send_confirmation_email(self, email):
        print(f"Sending order confirmation to {email}...")
```

> [!note]- Identify the Smell
> The `Order` class handles order calculations (`calculate_total`), order printing (`print_order`), and sending email confirmations (`send_confirmation_email`).

> [!note]- Explain the Problem
> The `Order` class has too many responsibilities. Changes to the email sending logic, the way the order is printed, or how the total is calculated would all require modifying this class.

> [!note]- Refactor
> Create separate classes for order printing and email confirmation.

```python
class Order:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def calculate_total(self):
        total = 0
        for i in range(len(self.items)):
            total += self.prices[i]
        return total

class OrderPrinter:
    def print_order(self, order):
        for i in range(len(order.items)):
            print(f"{order.items[i]}: ${order.prices[i]}")
        print(f"Total: ${order.calculate_total()}")

class EmailSender:
    def send_confirmation_email(self, order, email):
        # Code to send an order confirmation email
        print(f"Sending order confirmation to {email}...")

# Example usage
order = Order(["Item1", "Item2"], [10, 20])
printer = OrderPrinter()
printer.print_order(order)
sender = EmailSender()
sender.send_confirmation_email(order, "test@example.com")
```

**Task 3:**

```python
class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self, format):
        if format == "PDF":
            self.generate_pdf_report()
        elif format == "CSV":
            self.generate_csv_report()
        else:
            print("Invalid format.")

    def generate_pdf_report(self):
        # Code to create a PDF report from data
        print("Generating PDF report...")

    def generate_csv_report(self):
        # Code to create a CSV report from data
        print("Generating CSV report...")
```

> [!note]- Identify the Smell
> `ReportGenerator` handles multiple report formats within the same class. Adding a new format means modifying this class.

> [!note]- Explain the Problem
> Violates SRP. Changes to one report format might affect others.

> [!note]- Refactor
> Create separate classes for each report format.

```python
class ReportGenerator: #Abstract class
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        raise NotImplementedError
        
class PDFReportGenerator(ReportGenerator):
    def generate_report(self):
        # Code to create a PDF report from data
        print("Generating PDF report...")

class CSVReportGenerator(ReportGenerator):
    def generate_report(self):
        # Code to create a CSV report from data
        print("Generating CSV report...")

# Example usage
data = {"key": "value"}
pdf_generator = PDFReportGenerator(data)
pdf_generator.generate_report()
csv_generator = CSVReportGenerator(data)
csv_generator.generate_report()
```

**Task 4:**

```python
class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def calculate_average(self):
        pass #Some calculation here

    def calculate_standard_deviation(self):
        pass #Some calculation here
    
    def find_max(self):
        pass #Some calculation here
    
    def find_min(self):
        pass #Some calculation here

    def export_to_csv(self):
        print("Exporting data to CSV...")
```

> [!note]- Identify the Smell
> The `DataAnalyzer` class has multiple responsibilities: calculating statistics (`calculate_average`, `calculate_standard_deviation`, `find_max`, `find_min`) and exporting data (`export_to_csv`).

> [!note]- Explain the Problem
> The class violates SRP because changes to the export format or the addition of new statistical calculations would require modifying this single class.

> [!note]- Refactor
> Separate the data export functionality into a different class.

```python
class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        pass  # Some calculation here

    def calculate_standard_deviation(self):
        pass  # Some calculation here

    def find_max(self):
        pass  # Some calculation here

    def find_min(self):
        pass  # Some calculation here

class DataExporter:
    def export_to_csv(self, data):
        # Code to export the data to a CSV file
        print("Exporting data to CSV...")

# Example usage
data = [1, 2, 3, 4, 5]
analyzer = DataAnalyzer(data)
exporter = DataExporter()
exporter.export_to_csv(data)
```

### O - Open/Closed Principle (OCP)

**Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.**

**Task 1:**

```python
class DiscountCalculator:
    def __init__(self, discount_type, discount_value):
        self.discount_type = discount_type
        self.discount_value = discount_value

    def calculate_discount(self, price):
        if self.discount_type == "fixed":
            return price - self.discount_value
        elif self.discount_type == "percentage":
            return price - (price * self.discount_value / 100)
        else:
            return price
```

> [!note]- Identify the Smell
> The `calculate_discount` method has to be modified every time a new discount type is added.

> [!note]- Explain the Problem
> This violates the OCP because you need to change the existing class to add new functionality (new discount types).

> [!note]- Refactor
> Use inheritance to allow adding new discount types without modifying existing code.

```python
class DiscountCalculator:  # Base class for discounts
    def calculate_discount(self, price):
        raise NotImplementedError

class FixedDiscount(DiscountCalculator):
    def __init__(self, discount_value):
        self.discount_value = discount_value

    def calculate_discount(self, price):
        return price - self.discount_value

class PercentageDiscount(DiscountCalculator):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_discount(self, price):
        return price - (price * self.discount_percentage / 100)

# Example usage:
fixed_discount = FixedDiscount(10)
percentage_discount = PercentageDiscount(20)
print(fixed_discount.calculate_discount(100))
print(percentage_discount.calculate_discount(100))
```

**Task 2:**

```python
class Logger:
    def __init__(self, format):
        self.format = format

    def log(self, message):
        if self.format == "text":
            print(f"Log: {message}")
        elif self.format == "html":
            print(f"<p>Log: {message}</p>")
```

> [!note]- Identify the Smell
> The `log` method needs modification every time a new logging format is added.

> [!note]- Explain the Problem
> Violates OCP. Adding new logging formats requires changing the `Logger` class.

> [!note]- Refactor
> Create an interface (abstract class) for logging formats and separate
```python
class Logger: #Abstract class
    def log(self, message):
        raise NotImplementedError

class TextLogger(Logger):
    def log(self, message):
        print(f"Log: {message}")

class HTMLLogger(Logger):
    def log(self, message):
        print(f"<p>Log: {message}</p>")

# Example Usage
text_logger = TextLogger()
text_logger.log("This is a text log.")
html_logger = HTMLLogger()
html_logger.log("This is an HTML log.")
```

**Task 3:**

```python
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if shape_type == "circle":
            self.radius = kwargs["radius"]
        elif shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]

    def calculate_area(self):
        if self.shape_type == "circle":
            return 3.14 * self.radius * self.radius
        elif self.shape_type == "rectangle":
            return self.width * self.height
```

> [!note]- Identify the Smell
> The `Shape` class needs modification every time a new shape type is added. The constructor and `calculate_area` are especially affected.

> [!note]- Explain the Problem
> Violates OCP. Adding new shape types forces changes to the `Shape` class.

> [!note]- Refactor
> Use inheritance to create separate shape classes.
```python
import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.calculate_area())
print(rectangle.calculate_area())
```

**Task 4:**

```python
class Event:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

    def process_event(self):
        if self.event_type == "click":
            print(f"Processing click event: {self.data}")
        elif self.event_type == "scroll":
            print(f"Processing scroll event: {self.data}")
        # ... other event types ...
```

> [!note]- Identify the Smell
> The `process_event` method within the `Event` class needs modification every time a new event type is introduced.

> [!note]- Explain the Problem
> This violates the Open/Closed Principle (OCP) because you have to modify the existing `Event` class to add new event handling logic.

> [!note]- Refactor
> Create an interface (or abstract class) for event handlers and separate classes for each event type.

```python
class EventHandler:
    def process_event(self, data):
        raise NotImplementedError

class ClickEventHandler(EventHandler):
    def process_event(self, data):
        print(f"Processing click event: {data}")

class ScrollEventHandler(EventHandler):
    def process_event(self, data):
        print(f"Processing scroll event: {data}")

# Example usage
click_handler = ClickEventHandler()
scroll_handler = ScrollEventHandler()

click_event_data = {"x": 10, "y": 20}
scroll_event_data = {"delta": 5}

click_handler.process_event(click_event_data)
scroll_handler.process_event(scroll_event_data)
```

