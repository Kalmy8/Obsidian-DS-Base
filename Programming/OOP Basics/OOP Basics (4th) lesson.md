[[OOP Basics (3rd) lesson|<previous]]  |  [[OOP Basics (5th) lesson|next>]]
**Codewords:** SOlid principles

**Theory:** [[SOLID principles]]
**Practice:**

For each code snippet:

1. **Identify the Smell:** Carefully examine the code and identify the specific parts that violate the SOLID principle in question.
2. **Explain the Problem:** Describe *why* the code violates the principle and what problems this violation might cause.
3. **Refactor:** Rewrite the code to address the identified issues and make it adhere to the SOLID principle.

**Code Snippets and Solutions:**

**S - Single Responsibility Principle (SRP)**

*   **Definition:** A class should have only one specific reason to change.

**Code Snippet 1**

```python
class UserManager:
    def __init__(self, user_data):
        self.user_data = user_data

    def create_user(self, name, email):
        # Logic to create a new user in the database
        pass

    def update_user(self, user_id, new_name, new_email):
        # Logic to update user details
        pass

    def delete_user(self, user_id):
        # Logic to delete a user
        pass

    def save_user_data_to_csv(self, filename):
        # Logic to export user data to a CSV file
        pass

    def send_email_to_user(self, user_id, message):
        # Logic to send an email to a user
        pass
```

*   **Violations:** 
*   **Refactoring Suggestion:**

**Code Snippet 2**

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

    def apply_discount(self, discount_percent):
        total = self.calculate_total()
        return total - (total * discount_percent / 100)

    def generate_invoice_pdf(self, filename):
        # Logic to generate a PDF invoice from order details
        pass
```

*   **Violations:** 
*   **Refactoring Suggestion:** 

**Code Snippet 4**

```python
class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def load_data_from_csv(self, filepath):
        # Code to load data from CSV
        pass

    def clean_data(self):
        # Code to clean the data (handle missing values, etc.)
        pass

    def calculate_average(self, column_name):
        # Code to calculate the average of the specified column
        pass

    def plot_histogram(self, column_name):
        # Code to generate a histogram plot
        pass

    def export_results_to_json(self, filename):
        # Code to export results to a JSON file
        pass
```

*   **Violations:** 
*   **Refactoring Suggestion:** 

**Code Snippet 5**

```python
class Report:
    def __init__(self, content):
        self.content = content

    def format_to_html(self):
        # Code to format content as an HTML string
        pass

    def format_to_json(self):
        # Code to format content as a JSON string
        pass

    def format_to_xml(self):
        # Code to format content as an XML string
        pass

    def print_report(self):
        # Code to print the report to the console
        pass

    def save_report_to_file(self, filename):
        # Code to save the report to a file
        pass
```

*   **Violations:** 
*   **Refactoring Suggestion:** 

**O - Open/Closed Principle (OCP)**

*   **Definition:** Software entities (classes, modules, etc.) should be open for extension but closed for modification.

**Code Snippet 1**

```python
class DiscountCalculator:
    def __init__(self, customer_type):
        self.customer_type = customer_type

    def calculate_discount(self, amount):
        if self.customer_type == "normal":
            return amount * 0.1  # 10% discount
        elif self.customer_type == "premium":
            return amount * 0.2  # 20% discount
        # To add a new customer type, we need to modify this class.
```

*   **Violations:** 
*   **Refactoring Suggestion:** 

**Code Snippet 2**

```python
class ReportGenerator:
    def __init__(self, data, report_type):
        self.data = data
        self.report_type = report_type

    def generate_report(self):
        if self.report_type == "pdf":
            # Generate PDF report
            pass
        elif self.report_type == "html":
            # Generate HTML report
            pass
        # Adding new report types requires modifying this class
```

*   **Violations:** The `generate_report` method needs modification to support new report types.
*   **Refactoring Suggestion:** Create a base class `Report` and subclasses for each format (e.g., `PDFReport`, `HTMLReport`).

**Code Snippet 3**

```python
class EventLogger:
    def __init__(self, log_format):
        self.log_format = log_format

    def log_event(self, event):
        if self.log_format == "console":
            print(f"LOG: {event}")
        elif self.log_format == "file":
            with open("log.txt", "a") as f:
                f.write(f"LOG: {event}\n")
        # Adding new log formats means modifying this class.
```

*   **Violations:** The `log_event` method needs changes to support new logging formats.
*   **Refactoring Suggestion:** Create a base class `Logger` and subclasses for each format (e.g., `ConsoleLogger`, `FileLogger`).

**Code Snippet 4**

```python
class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_total_area(self):
        total_area = 0
        for shape in self.shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            elif isinstance(shape, Circle):
                total_area += 3.14 * shape.radius * shape.radius
        return total_area
```

*   **Violations:** Adding a new shape (e.g., `Triangle`) requires modifying `calculate_total_area`.
*   **Refactoring Suggestion:** Make `Shape` an abstract base class with an abstract `area()` method. Each shape subclass (e.g., `Rectangle`, `Circle`, `Triangle`) implements `area()`.

**Code Snippet 5**

```python
class NotificationSender:
    def __init__(self, notification_type):
        self.notification_type = notification_type

    def send_notification(self, message):
        if self.notification_type == "email":
            # Code to send an email
            pass
        elif self.notification_type == "sms":
            # Code to send an SMS
            pass
```

*   **Violations:** Adding a new notification type (e.g., "push") requires modifying `send_notification`.
*   **Refactoring Suggestion:** Create a base class `Notification` and subclasses for each type (e.g., `EmailNotification`, `SMSNotification`).

**L - Liskov Substitution Principle (LSP)**

*   **Definition:** Subtypes must be substitutable for their base types without altering the correctness of the program.

**Code Snippet 1**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

# Usage that violates LSP
def print_area(rect):
    rect.set_width(5)
    rect.set_height(4)
    print(f"Area: {rect.get_area()}")  # Expected 20 for Rectangle

rectangle = Rectangle(2, 3)
print_area(rectangle)  # Output: Area: 20 (Correct)

square = Square(2, 3)
print_area(square)  # Output: Area: 16 (Incorrect - a Square should still give area 20)
```

*   **Violations:** A `Square` cannot be used reliably in place of a `Rectangle` because changing the width or height of a square should always modify both.
*   **Refactoring Suggestion:**  `Square` should not inherit from `Rectangle`. Instead, consider a common interface or abstract base class for shapes.

**Code Snippet 2**

```python
class Bird:
    def fly(self):
        print("Flying")

class Eagle(Bird):
    def fly(self):
        print("Soaring through the sky")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
```

*   **Violations:** A `Penguin` cannot be substituted for a `Bird` if the code expects the `fly()` method to work.
*   **Refactoring Suggestion:**  Introduce a `FlightlessBird` class or remove the `fly()` method from the `Bird` class.

**Code Snippet 3**

```python
class Database:
    def connect(self):
        print("Connecting to database")

    def query(self, sql):
        print(f"Executing query: {sql}")
        return []

class ReadOnlyDatabase(Database):
    def connect(self):
        print("Connecting to read-only database")

    def query(self, sql):
        if sql.startswith("SELECT"):
            return super().query(sql)
        else:
            raise Exception("Write operations not allowed")
```

*   **Violations:** A `ReadOnlyDatabase` cannot be substituted for a `Database` if the code attempts to execute non-`SELECT` queries.
*   **Refactoring Suggestion:** Consider separate interfaces for read and write operations or different base classes.

**Code Snippet 4**

```python
class Document:
    def __init__(self, content):
        self.content = content

    def open(self):
        print("Opening document")

    def save(self):
        print("Saving document")

class ReadOnlyDocument(Document):
    def open(self):
        print("Opening read-only document")

    def save(self):
        raise Exception("Cannot save a read-only document")
```

*   **Violations:** A `ReadOnlyDocument` cannot be substituted for a `Document` if the code expects to be able to save it.
*   **Refactoring Suggestion:**  Perhaps have a separate interface or a method like `can_save()` to check capabilities.

**Code Snippet 5**

```python
class AudioPlayer:
    def play(self):
        print("Playing audio")

class WavPlayer(AudioPlayer):
    def play(self):
        print("Playing WAV file")

class Mp3Player(AudioPlayer):
    def play(self):
        raise Exception("MP3 playback not supported")
```

*   **Violations:** An `Mp3Player` cannot be substituted for an `AudioPlayer` if the code expects `play()` to function.
*   **Refactoring Suggestion:** Consider a more refined hierarchy or separate interfaces for different audio formats.

**I - Interface Segregation Principle (ISP)**

*   **Definition:** Clients should not be forced to depend on methods they do not use. Interfaces should be small and specific.

**Code Snippet 1**

```python
class AllInOnePrinter:
    def print_document(self, document):
        # Code to print
        pass

    def fax_document(self, document, number):
        # Code to fax
        pass

    def scan_document(self):
        # Code to scan
        pass

    def staple_document(self, document):
        # Code to staple
        pass

class BasicPrinter:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self, document):
        self.printer.print_document(document)
```

*   **Violations:** A `BasicPrinter` might not need `fax_document`, `scan_document`, or `staple_document`, but it is forced to depend on the `AllInOnePrinter` interface.
*   **Refactoring Suggestion:** Create separate interfaces: `Printer`, `Fax`, `Scanner`, `Stapler`.

**Code Snippet 2**

```python
class Shape:  # Too broad interface
    def draw_circle(self, radius):
        raise NotImplementedError

    def draw_rectangle(self, width, height):
        raise NotImplementedError

    def draw_triangle(self, base, height):
        raise NotImplementedError

class Circle(Shape):
    def draw_circle(self, radius):
        # Code to draw a circle
        pass

    def draw_rectangle(self, width, height):
        pass  # Does nothing, but forced to implement

    def draw_triangle(self, base, height):
        pass  # Does nothing, but forced to implement
```

*   **Violations:** `Circle` is forced to implement methods it doesn't need.
*   **Refactoring Suggestion:** Create separate interfaces: `CircleDrawer`, `RectangleDrawer`, `TriangleDrawer`.

**Code Snippet 3**

```python
class Worker:  # Too broad
    def work(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

    def sleep(self):
        raise NotImplementedError

class HumanWorker(Worker):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class RobotWorker(Worker):
    def work(self):
        print("Working")

    def eat(self):
        pass  # Robots don't eat, but forced to implement

    def sleep(self):
        pass  # Robots don't sleep, but forced to implement
```

*   **Violations:** `RobotWorker` is forced to implement methods it doesn't need.
*   **Refactoring Suggestion:** Separate interfaces: `Workable`, `Eatable`, `Sleepable`.

**Code Snippet 4**

```python
class DataProcessor:  # Too broad
    def load_data(self, source):
        raise NotImplementedError

    def clean_data(self):
        raise NotImplementedError

    def analyze_data(self):
        raise NotImplementedError

    def visualize_data(self):
        raise NotImplementedError

class SimpleDataProcessor:
    def __init__(self, data_processor):
        self.data_processor = data_processor
    
    def load_data(self, source):
        self.data_processor.load_data(source)
        
    def clean_data(self):
        self.data_processor.clean_data()

    def analyze_data(self):
        self.data_processor.analyze_data()
```

*   **Violations:** `SimpleDataProcessor` might only need to load and clean data, but it depends on the entire `DataProcessor` interface.
*   **Refactoring Suggestion:**  Separate interfaces: `DataLoader`, `DataCleaner`, `DataAnalyzer`, `DataVisualizer`.

**Code Snippet 5**

```python
class PaymentGateway:  # Too broad
    def process_credit_card(self, card_details):
        raise NotImplementedError

    def process_paypal(self, paypal_details):
        raise NotImplementedError

    def process_bank_transfer(self, bank_details):
        raise NotImplementedError

class SomeClient:
    def __init__(self, gateway):
        self.gateway = gateway

    def make_payment(self, payment_details):
        self.gateway.process_credit_card(payment_details)
```

*   **Violations:** `SomeClient` might only need to process credit cards but depends on the whole `PaymentGateway` interface.
*   **Refactoring Suggestion:** Separate interfaces: `CreditCardProcessor`, `PaypalProcessor`, `BankTransferProcessor`.

**D - Dependency Inversion Principle (DIP)**

*   **Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

**Code Snippet 1**

```python
class EmailSender:  # Low-level module
    def send_email(self, to_address, message):
        # Code to send an email using a specific email service
        pass

class NotificationService:  # High-level module
    def __init__(self):
        self.email_sender = EmailSender()  # Dependency on a concrete class

    def send_notification(self, to_address, message):
        self.email_sender.send_email(to_address, message)
```

*   **Violations:** `NotificationService` directly depends on the concrete `EmailSender` class.
*   **Refactoring Suggestion:** Introduce an interface (e.g., `NotificationSender`) and have both classes depend on it. Inject the dependency into `NotificationService`.

**Code Snippet 2**

```python
class FileLogger:  # Low-level
    def log(self, message):
        with open("app.log", "a") as f:
            f.write(message + "\n")

class ErrorHandler:  # High-level
    def __init__(self):
        self.logger = FileLogger()  # Dependency on concrete class

    def handle_error(self, error_message):
        self.logger.log(f"ERROR: {error_message}")
```

*   **Violations:** `ErrorHandler` directly depends on `FileLogger`.
*   **Refactoring Suggestion:** Introduce an interface (e.g., `Logger`) and inject the dependency.

**Code Snippet 3**

```python
class MySQLDatabase: # Low level
    def insert(self, data):
        # Code to insert into MySQL
        pass

    def update(self, id, data):
        # Code to update MySQL
        pass

class UserRepository: # High level
    def __init__(self):
        self.db = MySQLDatabase()

    def add_user(self, user):
        self.db.insert(user)

    def update_user(self, user_id, user):
        self.db.update(user_id, user)
```

*   **Violations:**  `UserRepository` is tightly coupled to `MySQLDatabase`.
*   **Refactoring Suggestion:** Introduce an interface (e.g., `Database`) and use dependency injection.

**Code Snippet 4**

```python
class XMLFormatter:
    def format(self, data):
        # Code to format data as XML
        pass

class ReportGenerator:
    def __init__(self):
        self.formatter = XMLFormatter()

    def generate_report(self, data):
        formatted_data = self.formatter.format(data)
        # ... further processing ...
```

*   **Violations:** `ReportGenerator` depends directly on the concrete `XMLFormatter`.
*   **Refactoring Suggestion:**  Introduce an interface (e.g., `DataFormatter`) and inject a formatter instance.

**Code Snippet 5**

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Turning on")

    def turn_off(self):
        print("LightBulb: Turning off")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()
        self.on = False

    def press(self):
        self.on = not self.on
        if self.on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()
```

*   **Violations:** `Switch` depends directly on the concrete `LightBulb` class.
*   **Refactoring Suggestion:**  Introduce an interface (e.g., `Switchable`) that both `LightBulb` (and potentially other devices) can implement. Inject a `Switchable` object into the `Switch`.

**Remember**:
The refactoring suggestions are just one way to address the SOLID principle violations. The best solution will depend on the specific context and the overall design of your system. Also, mention that the provided code is only a template, and may not be directly runnable without some adjustements. Encourage students to finish the code.
This collection of code snippets and explanations will give your students a practical understanding of how to identify and fix violations of SOLID principles in their code. By starting with code smells, they will develop an intuitive sense of why these principles are important for writing high-quality, maintainable software.
