#🃏/programming
What is a **Visitor** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Visitor** paradigm.
?
[Visitor.mhtml](Visitor.mhtml)
The **Visitor pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to handle some method invocation in all objects in some complex data structure like tree/graph/etc.
Let's say you need to add a new feature for all components inside your complex data structure, maybe for nodes in a tree. Let's say, each node now should print how many children it has, or print nothing if it is a **Leaf** subclass node. You have to modify each class inside your tree to have this `special_print(object)` method and apply all the real logic there, and hope that you won't accidently override something. Instead of doing this, you introduсe a **Visitor object** and implement the `special_print()` method there for each object using overriding. If your language does not support overriding, you can instead create a bunch of `print_leaf()`, `print_node()` methods. Your tree subclasses also need to implement one single `accept_visit()` method. This way, all the new feature implementation is included in a single visitor object, and all the old objects inside the tree need to implement just a single accept method, invoking new developed logic.
##### Visitor pattern structure
![Pasted image 20240906114506.png](Pasted%20image%2020240906114506.png)
The pattern itself consists of **4 main parts**:
1. **VisitorInterface (ABC):** class holding abstract `visit_class1()`, `visit_class2`,... methods to define for which classes you are creating a visitor.
2. **Component interface (ABC):**  usually carries just one single `accept(visitor:VisitorInterface)` method.
3. **Concrete Visitors:** a subclass of **VisitorInterface \[1]** which objects do implement some real OPERATION. The operation is the same for all of the different components, but the code differ slightly to handle the variaty. So a **concrete visitor is responsible for introducing one new feature**.
4. **Concrete components:** a subclass of **ComponentInterface\[2]**, concrete components are just your application classes with `accept()` method defined within them. The body of the `accept()` method contains according invokation inside a visitor. So, let's say, some `Leaf` object will have an `accept(visitor:PrintVisitor)` including `visitor.visit_leaf()` line.
##### When to use?
1. Use the Visitor when you need to perform an operation on all elements of a complex object structure (for example, an object tree).
2. Use the pattern when a behavior makes sense only in some classes of a class hierarchy, but not in others.
3. You can use visitor with Composite pattern to perform operations on tree elements.
4. You can use visitor with Iterator pattern to perform operations on Iterable's elements
##### Visitor pattern benefits
-  **Open/Closed Principle:** You can introduce a new behavior that can work with objects of different classes without changing these classes.
-  **Single Responsibility Principle**: You can move multiple versions of the same behavior into the same class.
-  A visitor object can accumulate some useful information while working with various objects. This might be handy when you want to traverse some complex object structure, such as an object tree, and apply the visitor to each object of this structure.
##### Visitor pattern mock-code example
```python
class Component(ABC):
    """
    The Component interface declares an `accept` method 
    that should take the base visitor interface as an argument.
    """
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentA(Component):
    """
    Each Concrete Component must implement the `accept` method 
    in such a way that it calls the visitor's method 
    corresponding to the component's class.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Note that we're calling `visitConcreteComponentA`, 
        which matches the current class name. This way we 
        let the visitor know the class of the
        component it works with.
        """
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Concrete Components may have special methods that 
        don't exist in their base class or interface. 
        The Visitor is still able to use these methods
        since it's aware of the component's concrete class.
        """
        return "A"

class ConcreteComponentB(Component):
    """
    Same here: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"

class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods 
    that correspond to component classes. 
    The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing 
    with.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass

"""
Concrete Visitors implement several versions of the same algorithm, which canwork with all concrete component classes.

You can experience the biggest benefit of the Visitor pattern when using it witha complex object structure, such as a Composite tree. In this case, it might be helpful to store some intermediate state of the algorithm while executing visitor's methods over various objects of the structure.
"""

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")

def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of 
    elements without figuring out their concrete classes. 
    The accept operation directs a call to
    the appropriate operation in the visitor object.
    """
    # ...
    for component in components:
        component.accept(visitor)
    # ...

components = [ConcreteComponentA(), ConcreteComponentB()]

print("The client code works with all visitors via \
the base Visitor interface:")
visitor1 = ConcreteVisitor1()
client_code(components, visitor1)

print("It allows the same client code to work with \
	  different types of visitors:")
visitor2 = ConcreteVisitor2()
client_code(components, visitor2)
```
<!--SR:!2026-06-05,467,310-->