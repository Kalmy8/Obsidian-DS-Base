#🃏/programming
What is a **Command pattern** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Command** paradigm.
?
[Command.mhtml](../../📁%20files/Command.mhtml)
The **Command pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to inroduce some mid **Command** layer which is responsible for  delivering user requests to some real worker (reciever). Remember the [Bridge pattern](Bridge%20pattern.md). Bridge pattern separates abstraction from the implementation. Every Abstraction has a set of features avaliable for a client (user interface), each feature is bonded and served with some methods which are implemented in concrete implementations (business logic). Now the Abstraction **(Invoker) is only responsible for pushing binded commands**, not invoking the implementation directly. **Every feature avaliable to user can be represented as a parametrized Command**. These commands are being initialized, binded to invokers and executed by **implementators (recievers)** then pushed. This complex structure is benefitial because:
1. Just like the bridge pattern, it decouples the business logic from the user interface, allowing both to develop independently. The recievers only need to provide some `execute(command)` method to be good to go with commands.
2. Commands are acting as a mid-layer, which is benefitial over the bridge pattern, because they can be treated as a separate object, **so be logged/un-done/re-done/queued and scheduled.**
##### Command pattern structure
![Pasted image 20240903110828.png](../../📁%20files/Pasted%20image%2020240903110828.png)
The pattern itself consists of **4 main parts**:
1. **Invoker:** a class which purpose is to invoke (send) binded commands, so they should have a field for referencing binded command/commands and a method to actually bind/unbind the command to themselves.
2. **Command (ABC):** an abstract class which usually defines the single method (e.g. `execute(self)`) for all of the concrete commands.
3. **Concrete Commands:** a subclass of **Command \[2]**, which implements the `execute(self)` method with all required logic, delegating the real work to the **Reciever \[4]**. Thus, it has to have a field reference to some reciever, which is usually initialized via `__init__`.
4. **Reciever:** a class which objects do implement all the methods needed to execute the defined **Concrete Commands \[3]**, contains all the business logic and doing all the actual work.
##### Command Pattern usage scenarios
You can benefit from using the pattern in following situations:
1. The **Command** pattern is particularly useful in scenarios where you have multiple invokers or interfaces that need to execute different commands in various ways. This is often the case in graphical user interfaces (GUIs) and complex systems where commands might be triggered by different events, user actions, or system states.
2. **Undo/Redo Functionality:** When you want to provide users with the ability to undo or redo actions.
3. **Queuing and Scheduling:** When you need to queue requests or schedule them for later execution.
4. **Parameterization:** When you want to pass requests as parameters to methods or store them in data structures.
5.  **Logging and Tracking:** When you need to keep a history of requests for auditing or debugging purposes.
##### Command pattern mock-code example
```python
# Abstract Command
class Command(ABC):
	def __init__(self, canvas: Canvas):
		self.canvas = Canvas
		
	@abstractmethod 
	def execute(self):
		pass

# Concrete Commands
class MoveLeft(Command):
	def execute(self):
		self.canvas.to_left()
	
class MoveRight(Command):
	def execute(self):
		self.canvas.to_right()

class Fire(Command):
	def execute(self):
		self.canvas.draw_bullet()
		
# Invoker
class Button(ABC):
	def __init__(self, command: Command):
		self.command = command

	def execute_command(self):
		self.command.execute()

# Reciever
class Canvas:
	@staticmethod 
	def draw_bullet():
		print("I have fired")
	@staticmethod 
	def to_left():
		print("I have leaned to the left")
	@staticmethod 
	def to_right():
		print("I have leaned to the right")


left_button = Button(MoveLeft())
right_button = Button(MoveRight())
fire_button = Button(Fire())

left_button.execute_command()
# Output: "I have leaned to the left"
```
