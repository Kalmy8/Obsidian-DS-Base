#🃏/programming
What is a **State** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **State** paradigm. Why is it similar and how is is it different from the [Strategy pattern](Strategy%20pattern.md)?
?
[State.mhtml](State.mhtml)
The **State pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to **switch some object's behavior depending on it's internal state**. Do you remember a classical finite-state machines, where the system has a defined number of states and some possible transitions between them? The state pattern looks just like that machine. Imagine that you are operating a smartphone. Your phone has a volume button on the edge, however, when the **phone is locked, this button just turns on a display**. **If the phone is already unlocked, it actually edit's the volume**. And **if you have entered a photo application, the volume button now acts like a shutter**. Of course, you always can hardcode all of this conditions right into your "VolumeButtonClass", but with such an approach things are likely to get messy as soon as you need to change the transition logic: that will involve changing ALL the defined if-else statements. Now Imagine that you are having several such classes, changing the transition logic then becomes a nightmare.
##### State pattern usage scenarios
1. **Order Processing:** An order goes through various states: Pending, Processing, Shipped, Delivered, Cancelled. Each state has different actions and transitions and would handle actions like updating the order status, sending notifications, or processing payments.
2. **Workflow Management Systems:** Tasks or items move through different stages in a workflow (e.g., bug tracking, content approval, data analysis pipelines). Each state defines the actions allowed, who can perform them, and how the task transitions to the next stage.
3. **In Data Science:** There is no common example of usage in Data Science.
##### State pattern structure
![Pasted image 20240906092838.png](Pasted%20image%2020240906092838.png)
The pattern itself consists of **3 main parts**:
1. **State and Context interface (ABC):**  abstract class defining some common operations which are meant to be processed differently within each state (like pressing the volume button on your phone). Both context class and concrete states are inherited from here, which guarantees that every method defined for user in Context Class will be served/implemented within State Classes.
2. **Context Class:** a subclass of **Shared interface \[1]**. Like in a [Strategy pattern](Strategy%20pattern.md), the context class carries all the methods avaliable for client, and delegates their implementation to the currently active **concrete state \[3] object**. It should **has some field in order to refer to the state so it would be assumed a current state**. It also can have some `changeState(state)` method which can be used to manually switch to the desired state.
3. **Concrete States:** a subclass of **State interface \[2]**, holding some actual business logic and concrete implementations. **Has some field to refer to the context class which now operates this state and a setter for it** in order to be able using context `changeState()` method and make a transition right into another state.
##### When to use?
1. Your object is meant to work differently according to the application state, states are clearly separable and the transitions can be defined.
2.  Your code is filled with many if-else statements to handle different object states, making it hard to read and maintain.
3. You have a lot of duplicate code across similar states and transitions of a condition-based state machine. Implementing some mid Abstract State classes and inheritance from them will help.
##### State pattern benefits
1.  **Single Responsibility Principle:**. Organize the code related to particular states into separate classes.
2.  **Open/Closed Principle:**. Introduce new states without changing existing state classes or the context.
3. Simplify the code of the context by eliminating bulky state machine conditionals.
##### State pattern mock-code example
```python
from __future__ import annotations

from abc import ABC, abstractmethod

class Phone(ABC):
    def __init__(self, initial_state : State):
        self.current_state = initial_state

    def set_state(self, state: State):
        self.current_state = state

    @abstractmethod 
    def press_back_button(self):
        """
        This abstract method enforces that all Phone subclasses
        must implement a way to handle the back button press.
        """
        pass 

# Defines possible operations
class State(ABC):
    @abstractmethod
    def handle_back_button(self, phone: Phone):
        """
        Handle the back button press according to the state's logic.
        """
        pass

class IsLocked(State):
    def handle_back_button(self, phone: Phone):
        print('Nothing happened')

class IsUnlocked(State):
    def handle_back_button(self, phone: Phone):
        print('Phone is now locked')
        phone.set_state(IsLocked())

class Realme(Phone):
    def press_back_button(self):
        self.current_state.handle_back_button(self)  # Delegate to state

# Usage (same as before)
```
#### State pattern and Strategy pattern
As you can see, state pattern seem to be very similar to the [Strategy pattern](Strategy%20pattern.md), and even the "Context Class" naming is the same. In reality, you can **think of a State pattern as to an extension of the Strategy pattern**, and here's why:
1. In Strategy Pattern, different strategies do not know each other and do not interact, but are used to implement same operation differently. In State pattern, states do know about each other and may invoke some transitions between them.
2. Usually, Strategy Pattern is logically binded to some concrete single operation (like Preprocessing an image, Loading a document...). State pattern, on the other side, usually defines a whole set of operations held differently depending of the current state.
<!--SR:!2025-10-16,271,290-->