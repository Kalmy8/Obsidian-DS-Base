[[OOP Basics (4th) lesson|<previous]]  |  [[OOP Basics (6th) lesson|next>]]
**Codewords:** soLID principles

**Theory:** [[SOLID principles]]
**Practice:**

For each code snippet:

1. **Identify the Smell:** Carefully examine the code and identify the specific parts that violate the SOLID principle in question.
2. **Explain the Problem:** Describe *why* the code violates the principle and what problems this violation might cause.
3. **Refactor:** Rewrite the code to address the identified issues and make it adhere to the SOLID principle.

### L - Liskov Substitution Principle (LSP)

**Definition:** Subtypes must be substitutable for their base types without altering the correctness of the program

**Task 1:**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
```

> [!note]- Identify the Smell
> The `Square` class, when its width or height is set, changes both dimensions, which might not be expected behavior when treating it as a `Rectangle`.

> [!note]- Explain the Problem
> Violates LSP. A `Square` cannot always be used in place of a `Rectangle` without potentially altering the program's behavior in unexpected ways. For instance, if you had a function that expected a `Rectangle` and tried to set the width and height independently, it would break if a `Square` was passed in.

> [!note]- Refactor
> One way to address this is to not have `Square` inherit from `Rectangle` if their behaviors are fundamentally incompatible. Another way (not shown here) is to have a more abstract `Shape` class that both can inherit from without implying that a square *is* a rectangle.

```python
# In this case, composition might be favored over inheritance
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square: #Does not inherit from Rectangle
    def __init__(self, side):
        self.side = side
    
    def set_side(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side
```

**Task 2:**

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
```

> [!note]- Identify the Smell
> The `Penguin` class's `fly` method raises an exception, which is unexpected behavior for a subclass of `Bird`.

> [!note]- Explain the Problem
> Violates LSP. A `Penguin` cannot be used in place of a `Bird` if the code expects the `fly` method to work without raising exceptions.

> [!note]- Refactor
> Create a separate hierarchy or interface for flightless birds.

```python
class Bird:
    def __init__(self, name):
        self.name = name

class FlyingBird(Bird):
    def fly(self):
        print(f"{self.name} is Flying")

class FlightlessBird(Bird):
    def walk(self):
        print(f"{self.name} is walking")

class Penguin(FlightlessBird):
    def __init__(self, name):
        super().__init__(name)
    

# Example usage
eagle = FlyingBird("Eagle")
eagle.fly()

penguin = Penguin("Emperor Penguin")
penguin.walk()
```

**Task 3:**

```python
class Document:
    def __init__(self, content):
        self.content = content

    def open(self):
        print(f"Opening document: {self.content}")

class ReadOnlyDocument(Document):
    def open(self):
        print(f"Opening document in read-only mode: {self.content}")

    def save(self):
        raise Exception("Cannot save a read-only document")
```

> [!note]- Identify the Smell
> The `ReadOnlyDocument` class inherits from `Document` but throws an exception in the `save` method, which is not expected behavior based on the base class.

> [!note]- Explain the Problem
> This violates the Liskov Substitution Principle. A `ReadOnlyDocument` object cannot be used as a substitute for a `Document` object because it breaks the expected contract (the ability to save).

> [!note]- Refactor
> Create separate interfaces for readable and writable documents or consider composition instead of inheritance if the behaviors are fundamentally different.

```python
class ReadableDocument:
    def __init__(self, content):
        self.content = content

    def open(self):
        print(f"Opening document: {self.content}")

class WritableDocument(ReadableDocument):
    def save(self):
        print(f"Saving document: {self.content}")

class ReadOnlyDocument(ReadableDocument):
    def open(self):
        print(f"Opening document in read-only mode: {self.content}")

# Example usage
readable_doc = ReadableDocument("Some content")
readable_doc.open()

writable_doc = WritableDocument("Other content")
writable_doc.open()
writable_doc.save()

read_only_doc = ReadOnlyDocument("Read-only content")
read_only_doc.open()
# read_only_doc.save()  # This would not be defined for a ReadOnlyDocument
```

### I - Interface Segregation Principle (ISP)

**Clients should not be forced to depend on methods they do not use. Interfaces should be small and specific.**

**Task 1:**

```python
class AllInOnePrinter:
    def print_document(self, document):
        pass
    def scan_document(self, document):
        pass
    def fax_document(self, document):
        pass
    def staple_document(self, document):
        pass
```

> [!note]- Identify the Smell
> The `AllInOnePrinter` class has methods for printing, scanning, faxing, and stapling. A simple printer that only prints would still need to implement (or at least have empty) these other methods.

> [!note]- Explain the Problem
> Violates ISP. Clients that only need printing are forced to depend on methods they don't use.

> [!note]- Refactor
> Break down the large interface into smaller, more specific interfaces.

```python
class Printer:
    def print_document(self, document):
        raise NotImplementedError

class Scanner:
    def scan_document(self, document):
        raise NotImplementedError

class Fax:
    def fax_document(self, document):
        raise NotImplementedError

class Stapler:
    def staple_document(self, document):
        raise NotImplementedError

# Example usage with specific devices
class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

class AdvancedPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")
    def scan_document(self, document):
        print(f"Scanning: {document}")
```

**Task 2:**

```python
class Worker:
    def work(self):
        pass
    def eat(self):
        pass
    def sleep(self):
        pass
```

> [!note]- Identify the Smell
> The `Worker` interface forces all workers to implement `work`, `eat`, and `sleep` methods, even if some workers (e.g., robots) don't need to eat or sleep.

> [!note]- Explain the Problem
> Violates ISP. Clients are forced to depend on methods they don't use.

> [!note]- Refactor
> Create smaller interfaces.

```python
class Workable:
    def work(self):
        raise NotImplementedError

class Eatable:
    def eat(self):
        raise NotImplementedError

class Sleepable:
    def sleep(self):
        raise NotImplementedError

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Working...")
    def eat(self):
        print("Eating...")
    def sleep(self):
        print("Sleeping...")

class RobotWorker(Workable):
    def work(self):
        print("Working...")

# Example usage
human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()
robot.work()
```

**Task 3:**

```python
class DriverManager:
    def manage_files(self):
        pass # e.g. copy, delete, move files
    def manage_cloud_storage(self):
        pass # e.g. upload, download files from cloud
    def manage_databases(self):
        pass # e.g. connect, query, update databases
    def manage_network(self):
        pass # e.g. configure network settings
```

> [!note]- Identify the Smell
> The `DriverManager` class has methods for managing files, cloud storage, databases, and network settings. A class using `DriverManager` might only need one of these functionalities but is forced to depend on all of them.

> [!note]- Explain the Problem
> This violates the Interface Segregation Principle (ISP) because clients are forced to depend on methods they do not use. It makes the `DriverManager` class large and complex, and changes to one area (e.g., database management) might affect unrelated parts.

> [!note]- Refactor
> Break down the large interface into smaller, more specific interfaces.

```python
class FileManager:
    def manage_files(self):
        pass  # e.g., copy, delete, move files

class CloudStorageManager:
    def manage_cloud_storage(self):
        pass  # e.g., upload, download files from cloud

class DatabaseManager:
    def manage_databases(self):
        pass  # e.g., connect, query, update databases

class NetworkManager:
    def manage_network(self):
        pass  # e.g., configure network settings

# Example usage (you can create specific classes that implement only the needed interfaces)
class FileAndCloudManager(FileManager, CloudStorageManager):
    def manage_files(self):
        print("Managing files...")

    def manage_cloud_storage(self):
        print("Managing cloud storage...")

manager = FileAndCloudManager()
manager.manage_files()
manager.manage_cloud_storage()
```

**Task 4:**

```python
class Shape:
    def draw(self):
        pass
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def serialize_to_json(self):
        pass
```

> [!note]- Identify the Smell
> The `Shape` class has methods for drawing, calculating area and perimeter, and serializing to JSON. A class using `Shape` might only need one of these functionalities (e.g., only drawing) but is forced to depend on all of them.

> [!note]- Explain the Problem
> This violates ISP because clients are forced to depend on methods they do not use. It makes the `Shape` class more complex and couples drawing logic with calculation and serialization logic.

> [!note]- Refactor
> Create smaller interfaces.

```python
class Drawable:
    def draw(self):
        raise NotImplementedError

class Calculable:
    def calculate_area(self):
        raise NotImplementedError
    
    def calculate_perimeter(self):
        raise NotImplementedError

class Serializable:
    def serialize_to_json(self):
        raise NotImplementedError

class Circle(Drawable, Calculable, Serializable):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        print("Drawing a circle")
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def serialize_to_json(self):
        print('serializing circle to json')

# Example usage
circle = Circle(5)
circle.draw()
print(circle.calculate_perimeter())
circle.serialize_to_json()
```

### D - Dependency Inversion Principle (DIP)

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

**Task 1:**

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: ON")

    def turn_off(self):
        print("LightBulb: OFF")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb
        self.on = False

    def operate(self):
        self.on = not self.on
        if self.on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()
```

> [!note]- Identify the Smell
> The `Switch` class directly depends on the concrete `LightBulb` class.

> [!note]- Explain the Problem
> Violates DIP. The high-level `Switch` class is tightly coupled to the low-level `LightBulb` class. If you wanted to use the `Switch` with a different device (e.g., a fan), you'd have to modify the `Switch` class.

> [!note]- Refactor
> Introduce an abstraction (interface) that both the `Switch` and `LightBulb` depend on.

```python
class Switchable: #Interface
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: ON")

    def turn_off(self):
        print("LightBulb: OFF")

class Switch:
    def __init__(self, device):
        self.device = device
        self.on = False

    def operate(self):
        self.on = not self.on
        if self.on:
            self.device.turn_on()
        else:
            self.device.turn_off()

# Example usage
bulb = LightBulb()
switch = Switch(bulb)
switch.operate()
switch.operate()
```

**Task 2:**

```python
class XMLReportGenerator:
    def generate_report(self, data):
        # Code to generate an XML report
        print("<report>...</report>")  # Placeholder

class Report:
    def __init__(self, data):
        self.data = data
        self.generator = XMLReportGenerator()

    def generate(self):
        self.generator.generate_report(self.data)
```

> [!note]- Identify the Smell
> The `Report` class directly depends on the concrete `XMLReportGenerator` class.

> [!note]- Explain the Problem
> Violates DIP. The high-level `Report` class is tightly coupled to the low-level `XMLReportGenerator`. Changing the report format would require modifying the `Report` class.

> [!note]- Refactor
> Introduce an abstraction for report generators and inject the dependency.

```python
class ReportGenerator: #Interface
    def generate_report(self, data):
        raise NotImplementedError

class XMLReportGenerator(ReportGenerator):
    def generate_report(self, data):
        print("<report>...</report>")  # Placeholder

class JSONReportGenerator(ReportGenerator):
    def generate_report(self, data):
        print("{report: ...}")

class Report:
    def __init__(self, data, generator):
        self.data = data
        self.generator = generator

    def generate(self):
        self.generator.generate_report(self.data)

# Example usage
data = {"key": "value"}
xml_generator = XMLReportGenerator()
json_generator = JSONReportGenerator()
report1 = Report(data, xml_generator)
report1.generate()
report2 = Report(data, json_generator)
report2.generate()
```

**Task 3:**

```python
class FileSystem:
    def read_file(self, filename):
        # Code to read a file from the file system
        print(f"Reading from file: {filename}")

    def write_file(self, filename, data):
        # Code to write data to a file
        print(f"Writing to file: {filename}")

class DataProcessor:
    def __init__(self):
        self.file_system = FileSystem()

    def process_data(self, input_file, output_file):
        data = self.file_system.read_file(input_file)
        # ... process the data ...
        processed_data = data
        self.file_system.write_file(output_file, processed_data)
```

> [!note]- Identify the Smell
> The `DataProcessor` class directly depends on the concrete `FileSystem` class.

> [!note]- Explain the Problem
> This violates the Dependency Inversion Principle (DIP). The high-level `DataProcessor` class is tightly coupled to the low-level `FileSystem` class. If you wanted to use a different data source or destination (e.g., a network socket, a database), you'd have to modify the `DataProcessor` class.

> [!note]- Refactor
> Introduce an abstraction for data access and inject the dependency.

```python
class DataAccessor:
    def read_data(self, source):
        raise NotImplementedError

    def write_data(self, destination, data):
        raise NotImplementedError

class FileSystem(DataAccessor):
    def read_data(self, filename):
        # Code to read a file from the file system
        print(f"Reading from file: {filename}")
        return "data from file"  # Placeholder

    def write_data(self, filename, data):
        # Code to write data to a file
        print(f"Writing to file: {filename}")

class DataProcessor:
    def __init__(self, data_accessor):
        self.data_accessor = data_accessor

    def process_data(self, source, destination):
        data = self.data_accessor.read_data(source)
        # ... process the data ...
        processed_data = data + " processed"
        self.data_accessor.write_data(destination, processed_data)

# Example usage
file_system = FileSystem()
processor = DataProcessor(file_system)
processor.