---
type: note
status: done
tags: ['tech/python']
sources:
-
- "[[Refactoring Guru - Design Patterns]]"
authors:
-
---
#🃏/semantic/design-patterns #🃏/refactoring-guru/design-patterns

What is a **Observer** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Observer** paradigm.
?
[Observer.mhtml](../../📁%20files/Observer.mhtml)
The **Observer pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to hande **one-to-many** dependencies, when you have a lot of dependent (subscribers/observers) and one independent (subject) objects in your application. Observers keep track of the subject, by some pull requests, or get notified by a subject with some sort of a push request. This way, when something important happens in the subject, changing it's state, observers which are subscribed on this event get a notification and do react on it in a desired way.
> You can think of an Observer pattern as of a callback-technique, but being more formal and general. You just subscribe created objects to react automatically on specific events.
##### Observer pattern usage scenarios
1. GUI components (subjects) and EventHandlers (observers) react when a user presses the button, enters the text, etc.
2. Callback mechanisms (accepting new users connections on a webserver, saving checkpoints while teaching an ML model) can also be realised as a special implementation of an Observer pattern.
3. Live auto-updated data dashboards.
##### Observer pattern structure
![Pasted image 20240906084655.png](Pasted%20image%2020240906084655.png)
The pattern itself consists of **4 main parts**:
1. **Subject interface (ABC):** class implementing at least **attach, detach and notify** methods for the subject, so it will be ready for working with observers.
2. **Subject:** a subclass of **Subject interface \[1]**, the working object of the application, which state is changing somehow (that's called an ***event***) and which has to notify the subscribers when it happens. It usually contains some business logic itself.
3. **Obsever interface (ABC):** a common interface for all of the observers, usually defining some single `update(state/Subject)` method, which is used by the subject to notify an observer of it's changes. Usually, the observers have to operate some additional information to react accrodingly to the event, so the `update(state/Subject)` method will have some ***state*** as a parameter, or even ***Subject*** as a parameter, so they can obtain the information by themselves.
4. **Concrete Observers:** a subclass of **Obsever interface \[2]** which objects do implement some real working logic, and **are being invoked by subject notifications**.
##### When to use?
1. You have a one-to-many dependency in your application and want to handle it properly.
2. Your application looks like an event-driven one, so you have to keep track of some events and react accordingly.
##### Observer pattern benefits
1. **Loose Coupling:** The Stock object doesn't need to know the concrete types of its observers or how they react to price changes.
2. **Dynamic Relationships:** You can add or remove observers at runtime.
3. **Open/Closed Principle:** You can introduce new types of observers without modifying the Stock class.
##### Observer pattern mock-code example
```python
class Subject(ABC):
---
 """
 The Subject interface declares a set of methods 
 for managing subscribers.
 """

 @abstractmethod
 def attach(self, observer: Observer) -> None:
 """
 Attach an observer to the subject.
 """
 pass

 @abstractmethod
 def detach(self, observer: Observer) -> None:
 """
 Detach an observer from the subject.
 """
 pass

 @abstractmethod
 def notify(self) -> None:
 """
 Notify all observers about an event.
 """
 pass

class ConcreteSubject(Subject):
 """
 The Subject owns some important state and notifies 
 observers when the state changes.
 """

 _state: int = None
 """
 For the sake of simplicity, the Subject's state, 
 essential to all subscribers, is stored in this variable.
 """

 _observers: List[Observer] = []
 """
 List of subscribers. In real life, the list of subscribers 
 can be stored more comprehensively 
 (categorized by event type, etc.).
 """

 def attach(self, observer: Observer) -> None:
 print("Subject: Attached an observer.")
 self._observers.append(observer)

 def detach(self, observer: Observer) -> None:
 self._observers.remove(observer)

 """
 The subscription management methods.
 """

 def notify(self) -> None:
 """
 Trigger an update in each subscriber.
 """

 print("Subject: Notifying observers...")
 for observer in self._observers:
 observer.update(self)

 def some_business_logic(self) -> None:
 """
 Usually, the subscription logic is only a fraction 
 of what a Subject can really do. Subjects commonly 
 hold some important business logic, that
 triggers a notification method whenever something 
 important is about to happen (or after it).
 """

 print("\nSubject: I'm doing something important.")
 self._state = randrange(0, 10)

 print(f"Subject: My state has just changed to: 
 {self._state}")
 self.notify()

class Observer(ABC):
 """
 The Observer interface declares the update method, 
 used by subjects.
 """

 @abstractmethod
 def update(self, subject: Subject) -> None:
 """
 Receive update from subject.
 """
 pass

"""
Concrete Observers react to the updates issued by 
the Subject they had been attached to.
"""

class ConcreteObserverA(Observer):
 def update(self, subject: Subject) -> None:
 if subject._state < 3:
 print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
 def update(self, subject: Subject) -> None:
 if subject._state == 0 or subject._state >= 2:
 print("ConcreteObserverB: Reacted to the event")

subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
# Output: somebody has reacted
subject.some_business_logic()
# Output: somebody has reacted
subject.detach(observer_a)

subject.some_business_logic()
# Output: Observer_B could have reacted
```
<!--SR:!2026-03-19,357,290-->