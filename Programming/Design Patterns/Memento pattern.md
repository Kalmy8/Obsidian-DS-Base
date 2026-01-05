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
#🃏/semantic/design-patterns #🃏/source/refactoring-guru/design-patterns

What is a **Memento pattern** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Memento** paradigm.
?
[Memento.mhtml](../../📁%20files/Memento.mhtml)
The **Memento pattern** is a [behavioral pattern](Behavioral%20patterns.md) which **special purpose is to save, store and revert some object's state** in a safe way (without exposing it's private fields).
##### Memento pattern structure
![Pasted image 20240904122535.png](Pasted%20image%2020240904122535.png)
The pattern itself consists of **4 main parts**:
1. **Originator:** the original object which state we do want to save and revert. So, the originator has to implement `save()` and `restore(memento)` methods which will create the **Concrete Memento \[3]** and restore it's state from the memento when needed.
2. **Memento (ABC):** abstract class declaring an interface for **only Memento-Caretaker\[2]** relationships, so the client won't be able to obtain hidden state which is stored inside a Memento, but will be able to use all other merhods returning additional information like `get_name(self)`, `get_date(self)`...
3. **Concrete Memento:** a subclass of **Memento \[2]**, which **implements all the defined methods plus one method that will be responsible for Memento-Originator relationship**. It is usually called something like `get_state(self)` and should return a hidden state that was passed to a memento during it's creation.
4. **Caretaker:** utility class actually implementing operations with saved Mementos, like re-doing, un-doing, making backups and showing history.
##### Memento pattern mock-code example
```python
class Originator:
---
 """
 The Originator holds some important state that may change 
 over time. It also defines a method for saving the state 
 inside a memento and another method for restoring the state 
 from it.
 """
 
 _state = None
 """
 For the sake of simplicity, the originator's state is 
 stored inside a single variable.
 """

 def __init__(self, state: str) -> None:
 self._state = state
 print(f"Originator: My initial state is: {self._state}")

 def do_something(self) -> None:
 """
 The Originator's business logic may affect its 
 internal state. Therefore, the client should backup 
 the state before launching methods of the business 
 logic via the save() method.
 """

 print("Originator: I'm doing something important.")
 self._state = self._generate_random_string(30)
 print(f"Originator: and my state has 
 changed to: {self._state}")

 @staticmethod
 def _generate_random_string(length: int = 10) -> str:
 return "".join(sample(ascii_letters, length))

 def save(self) -> Memento:
 """
 Saves the current state inside a memento.
 """
 return ConcreteMemento(self._state)

 def restore(self, memento: Memento) -> None:
 """
 Restores the Originator's state from a memento object.
 """
 self._state = memento.get_state()
 print(f"Originator: My state has changed to: 
 {self._state}")

class Memento(ABC):
 """
 The Memento interface provides a way to retrieve the 
 memento's metadata, such as creation date or name. 
 However, it doesn't expose the Originator's state.
 """

 @abstractmethod
 def get_name(self) -> str:
 pass

 @abstractmethod
 def get_date(self) -> str:
 pass

class ConcreteMemento(Memento):
 def __init__(self, state: str) -> None:
 self._state = state
 self._date = str(datetime.now())[:19]

 def get_state(self) -> str:
 """
 The Originator uses this method when restoring its state.
 """
 return self._state

 def get_name(self) -> str:
 """
 The rest of the methods are used by the Caretaker
 to display metadata.
 """

 return f"{self._date} / ({self._state[0:9]}...)"

 def get_date(self) -> str:
 return self._date

class Caretaker:
 """
 The Caretaker doesn't depend on the Concrete Memento class. 
 Therefore, it doesn't have access to the originator's state, 
 stored inside the memento. It works with all mementos via 
 the base Memento interface.
 """

 def __init__(self, originator: Originator) -> None:
 self._mementos = []
 self._originator = originator

 def backup(self) -> None:
 print("\nCaretaker: Saving Originator's state...")
 self._mementos.append(self._originator.save())

 def undo(self) -> None:
 if not len(self._mementos):
 return
 
 memento = self._mementos.pop()
 print(f"Caretaker: Restoring state to: 
 {memento.get_name()}")
 
 try:
 self._originator.restore(memento)
 except Exception:
 self.undo()

 def show_history(self) -> None:
 print("Caretaker: Here's the list of mementos:")
 for memento in self._mementos:
 print(memento.get_name())

originator = Originator("Super-duper-super-puper-super.")
caretaker = Caretaker(originator)

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

caretaker.backup()
originator.do_something()

print()
caretaker.show_history()

print("\nClient: Now, let's rollback!\n")
caretaker.undo()

print("\nClient: Once more!\n")
caretaker.undo()
```
<!--SR:!2026-11-28,365,290-->