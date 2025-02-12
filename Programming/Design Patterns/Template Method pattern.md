#🃏/programming
What is a **Template Method** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Template Method** paradigm.
?
[Template Method.mhtml](Template%20Method.mhtml)
The **Template Method pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to define some skeleton step-divised algorthim (a pipeline) while giving you an instrument to override some (or all) of it's steps, but not the pipeline itself. These one are actually very popular in data science sphere. Imagine that you are willing to preprocess some data, which includes Dropping Duplicates, Feature Selection, Missing values imputing and Scaling. Some of this steps can be implemented differently (you have multiple Imputing and scaling techniques), some of the steps are almost always implemented uniformally (like Dropping duplicates, which is just using pandas `dropna()` function).
##### Template pattern usage scenarios
1. ML models build, optimization, evaluation pipelines.
1. Preprocessing pipelines.
2. Report Generation Pipelines: You need to generate reports from data, involving steps like data retrieval, aggregation, formatting, and rendering. Different reports can have their own data sources, aggregation methods, formatting rules, and output formats while still adhering to the same report generation process.
##### Template pattern structure
![Pasted image 20240906105012.png](Pasted%20image%2020240906105012.png)
The pattern itself consists of **2 main parts**:
1. **Template:** abstact or non-abstract class implementing all the default methods and defining the sequence they are meant to be used (a pipeline). The pipeline is defined with just one method usually called `process()`. This class also can have some empty optional methods which are invoked before or after certain steps in the pipeline, they are usually called **hooks**. Concrete implementations can override this hooks also, including additional steps to the algorithm.
2. **Concrete implementations:**  a subclass of **Template**, overriding the default methods, but not the main `process()` method.
##### When to use?
1. You are dealing with some sort of a pipeline, so you have a step-divised algorthim to implement.
2. Use the pattern to unite several classes that contain almost identical algorithms with some minor differences in a template. As a result, you won't need to modify all classes when the algorithm changes.
#####  Pattern benefits
1. All duplicated code for your algorthims can be put in an abstract class and be shared.
2. Template pattern is user-friendly, as it makes all the required and optional steps easy-visible and obvious.
##### Template pattern mock-code example
```python
class AbstractClass(ABC):
    """
    The Abstract Class defines a template method that 
    contains a skeleton of some algorithm, composed of 
    calls to (usually) abstract primitive operations.

    Concrete subclasses should implement these operations, 
    but leave the template method itself intact.
    """

    def template_method(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # These operations already have implementations.

    def base_operation1(self) -> None:
        print("I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.
    
    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # These are "hooks." Subclasses may override them, 
    # but it's not mandatory since the hooks already have
    # default (but empty) implementation. 
    
    # Hooks provide additional extension points in some 
    #crucial places of the algorithm.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations
    of the base class. They can also override some 
    operations with a default implementation.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes override only a fraction 
    of base class operations.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")

def client_code(abstract_class: AbstractClass) -> None:
    """
    The client code calls the template method to execute 
    the algorithm. Client code does not have to know 
    the concrete class of an object it works with, as
    long as it works with objects through the interface of their 
    base class.
    """

    # ...
    abstract_class.template_method()
    # ...

print("Same client code can work with different subclasses:")
client_code(ConcreteClass1())
print("")

print("Same client code can work with different subclasses:")
client_code(ConcreteClass2())
```
<!--SR:!2025-03-30,148,310-->