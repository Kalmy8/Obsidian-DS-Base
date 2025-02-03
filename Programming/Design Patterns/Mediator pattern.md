#🃏/programming
What is a **Mediator pattern** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Mediator** paradigm.
?
[Mediator.mhtml](../../📁%20files/Mediator.mhtml)
The **Mediator pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to introduce a special **Mediator** object responsible for in-between objects communication. Imagine that you have some complex  set of classes, referencing each other and invoking each other's methods. Whole system when is quite a mess, the elements are tight-coupled, introducing new features and refactoring become a huge problem, because small changes in one class can cause all other classes to stop working. Instead of classes communicating directly, you use a Mediator object, so all the classes now only communicate with him, and he handles all of requests traffic. You can imagine yourself a conductor in an orchestra, who organises all musicians together and keeps them synchronized with each other. Without a conductor, an orchestra would fail to keep the required pace.
##### Iterator pattern structure
![Pasted image 20240904111221.png](../../📁%20files/Pasted%20image%2020240904111221.png)
The pattern itself consists of **4 main parts**:
1. **Mediator interface (ABC):** a common interface for all of the application mediators, if there are several ones. Commonly declares just one method like `notify(sender, event)`  used by components to notify the mediator about various events.
2. **Base Component interface (ABC):** a common interface for all of the application components, which simply declares a method to **bind the Component and some abstract Mediator**. This is usually being done via initialization.
3. **Concrete Mediator:** a subclass of **Mediator \[1]**, which implements all the Mediator's logic and reaction on different events. **The Mediator usually just needs to implement single `notify(sender, evenets)` method**, which holds all desired reactions for all possible events. **Usually, a Mediator will only invoke some other binded components to do some real work**, being responsible only for object communications, not implementing any real business logic.
4. **Concrete Component:** a subclass of **Base Component  \[2]** which objects do implement some real working logic, and **are being invoked by client or by Mediator object **.
You can benefit from using the pattern in following situations:
1. You have a complex class system with lot of traffic passing from one objects to the other ones in a variaty of directions.
2. You want to decouple a bunch of system components from each other, making them re-usable and extendible.
##### Mediator pattern mock-code example
```python
from abc import ABC

class Mediator(ABC):
    """
    The Mediator interface declares a method used by components 
    to notify the mediator about various events. 
    The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers \ 
            following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers \
            following operations:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    """
    The Base Component provides the basic functionality 
    of storing a mediator's instance inside component objects.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator
        
"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()
# Output : Component 1 does A.
# Mediator reacts on A and triggers following operations:
# Component 2 does C.

print("Client triggers operation D.")
c2.do_d()
# Client triggers operation D.
# Component 2 does D.
# Mediator reacts on D and triggers following operations:
# Component 1 does B.
# Component 2 does C.
```
<!--SR:!2025-04-05,122,270-->