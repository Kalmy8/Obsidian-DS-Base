#🃏/oop-basics 
Name each of the SOLID principles. For each principle, describe benefits of it's usage and provide a simple example of the principle violation/comitement
?
Let's break down each SOLID principle, exploring their benefits and illustrating both violations and good practices with simple Python examples:
**1. Single Responsibility Principle (SRP)**
   - **Description:** A class/module/function/service should have one, and only one, reason to change. In other words, a class should have only one job or responsibility.
   - **Benefits:**
      - **Increased Cohesion:** Makes classes more focused and understandable.
      - **Reduced Coupling:**  Minimizes dependencies between classes, making them easier to change independently.
      - **Improved Maintainability:**  Easier to find, fix, and extend code when classes have a clear purpose.
   - **Violation Example:**
```python
class Employee:
	def calculate_salary(self):
	 # ...
	def generate_report(self):
	 # ...
	def send_email(self):
	 # ... 
```
The `Employee` class has multiple responsibilities (salary calculation, report generation, email sending).
   - **Commitment Example:**
```python
class SalaryCalculator:
	def calculate_salary(self):
	 # ...
class ReportGenerator:
	def generate_report(self):
	 # ...
class EmailSender:
	def send_email(self):
	 # ... 
```
Responsibilities are separated into distinct classes.
**2. Open/Closed Principle (OCP)**
   - **Description:** Software entities (classes, modules, functions) should be open for extension, but closed for modification.
   - **Benefits:**
     - **Flexibility:** You can add new features or behaviors without changing existing code.
     - **Stability:** Reduces the risk of introducing bugs in existing code when extending functionality.
   - **Violation Example:**
```python
	class AreaCalculator:
		def calculate_area(self, shape):
			if isinstance(shape, Rectangle):
				return shape.width * shape.height
			elif isinstance(shape, Circle):
				return 3.14 * shape.radius**2
			# Add more if-else for new shapes 
```
Adding new shapes requires modifying the `calculate_area` method.
   - **Commitment Example:**
```python
	class Shape(ABC):
		@abstractmethod
		def calculate_area(self):
			 pass
			 
	class Rectangle(Shape):
		def calculate_area(self):
			 # (implements calculate_area)
		
	class Circle(Shape):
		def calculate_area(self):
			 # (implements calculate_area)
				
	class AreaCalculator:
		def calculate_area(self, shape: Shape):
			return shape.calculate_area()
```
New shapes can be added by creating new subclasses of `Shape` without modifying `AreaCalculator`.
**3. Liskov Substitution Principle (LSP)**
   - **Description:**  Subtypes should be substitutable for their base types without altering the correctness of the program.
   - **Benefits:**
      - **Predictability:** Ensures that subclasses behave as expected when used in place of their base classes.
      - **Polymorphism:** Allows you to use subtypes interchangeably without introducing errors.
   - **Violation Example:**
```python
	class Bird:
		def fly(self):
			 print("Flying!")
			 
	class Penguin(Bird): 
		def fly(self):
			raise NotImplementedError("Penguins can't fly")
			
	def make_bird_fly(bird: Bird):
		bird.fly()
		penguin = Penguin()
		make_bird_fly(penguin) # Raises an error!
```
The `Penguin` subclass breaks the expectation set by the `Bird` base class.
   - **Commitment Example:**
```python
	class Bird(ABC):
		@abstractmethod
		def move(self):
			pass
			
	class FlyingBird(Bird):
		def move(self):
			print("Flying!") 
			
	class Penguin(Bird):
		def move(self):
			print("Waddling!") 
		
	def make_bird_move(bird: Bird):
		bird.move()
```
Subclasses adhere to the contract of the base class (`move`), even if they implement it differently.
**4. Interface Segregation Principle (ISP)**
   - **Description:** Clients should not be forced to depend on methods they don't use. It's better to have multiple, smaller, client-specific interfaces than one large, general-purpose interface.
   - **Benefits:**
      - **Reduced Coupling:**  Clients only depend on the methods they need.
      - **Increased Flexibility:**  Changes to unused methods don't affect clients.
   - **Violation Example:**
```python
	class Worker:
		def work(self):
			pass
			
		def eat(self):
			pass
			
		def sleep(self):
			pass
			
	class Robot(Worker): # Robots don't eat or sleep
		# ... (implementation)
```
The `Robot` class is forced to implement methods (`eat`, `sleep`) it doesn't need.
   - **Commitment Example:**
```python
	class Workable(ABC):
		def work(self):
			pass

	class Eatable(ABC):
		def eat(self):
			pass

	class Sleepable(ABC):
		def sleep(self):
			pass

	class Human(Workable, Eatable, Sleepable):
		# ... (implementation)

	class Robot(Workable):
		# ... (implementation)
```
Interfaces are more focused, and classes only implement what they need.
**5. Dependency Inversion Principle (DIP)**
   - **Description:**
      - High-level modules should not depend on low-level modules. Both should depend on abstractions.
      - Abstractions should not depend on details. Details should depend on abstractions.
   - **Benefits:**
     - **Reduced Coupling:** Makes modules more independent and reusable.
     - **Improved Testability:** Easier to test modules in isolation.
   - **Violation Example:**
```python
	class LightBulb:
		def __init__(self):
			self.is_on = False
			
		def turn_on(self):
			print("Lightbulb ON")
			
		def turn_off(self):
			print("Lightbulb OFF")
			
	class Switch:
		def __init__(self, bulb: LightBulb):
			self.bulb = bulb
			
		def flip(self):
			if self.bulb.is_on:
				self.bulb.turn_off() 
			elif not self.bulb.is_on: 
				self.bulb.turn_on()
```
The `Switch` class is tightly coupled to the `LightBulb` class.
   - **Commitment Example:**
```python
	class Switchable(ABC):
		@abstractmethod
		def turn_on(self):
			pass
			
		@abstractmethod
		def turn_off(self):
			pass
			
	class LightBulb(Switchable): 
		# ... (implementation)
		
	class Switch:
		def __init__(self, device: Switchable):
			self.device = device
			
		def flip(self):
			# ... 
```
Both `Switch` and `LightBulb` depend on the `Switchable` abstraction.
**Remember:**  SOLID principles are guidelines, not rules.  Use them to make your code more maintainable, but don't be afraid to make trade-offs based on the complexity of your project.
