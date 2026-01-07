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

What is a **Decorator** design pattern? When is it useful and how would you know if you will benefit from utilizng it? How is it different from python @decorator syntaxis? Provide some mock-code example of a class designed within a **Decorator** paradigm.
?
[](Decorator.mhtml)
The **Decorator pattern** is a [Structural patterns](Structural%20patterns.md), which allows you to **extend some method/class behavior without actually modifying it or creating any subclasses**. It sort of **wraps** the inner class with some additional logic, executed **before or after the inner class logic**, the wrapped class is called a **wrappee**. It is yet simple and useful, allowing you to change any function's behaviour on fly, and even **stack a few decorators together, if needed**. Some usage examples may include:
1. Building pipelines. As every decorator and the base class share the same interface, you can implement some **transform** method in them and stack decorators as you need: `Imputer(Scaler((Standartizer())))`
---
1. Logging and evaluating ML models, so you can compare them easily with no need to create any extensive code.
3. Timing measurement, applying some timer decorator, which allow you to evaluate your code perfomance.
4. Caching any function results, which is also possible via implementing or using a built-in decorators (in python - "\@functools.cache").
5. Viewing intermediate results of your preprocessing pipeline.
##### Decorator pattern structure
In python, the decorator can be constructed as a function recieving an other function, and the language itself has some nice syntaxis sugar (the '@decorator') for convinient usage. However, the general decorator pattern is more complex than that and can be represented as rather a whole class.
The pattern itself consists of **4 main parts**:
[](Pasted%20image%2020240830172425.png)
1. **"Interface" Component**: an abstract class, defining some shared interface for all of the decorators and the decorated class, allowing for chaining and interchanging them.
2. **Concrete Component**: a class implementing some basic methods/behavior, which then could be extended with decorators.
3. **Basic Decorator**: an abstract class, extending the **"Interface" \[1]** class by adding some pointer (field, attribute) to actually refrence a wrapped object and invoke operations within it when being called.
4. **Concrete decorators**: actual classes, implementing methods defined in a **Basic Decorator \[3]** class. As a rule: the implementation of the method have to invoke the same method in a **wrapped** object.
##### Decorator pattern usage scenarios
You can benefit from using the pattern in following situations:
1. You need to be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.
2. It’s awkward or not possible to extend an object’s behavior using inheritance.
3. You want the **decorated behavior** be applicable to **multiple** functions or methods sharing the same interface
4. You need to enforce **pre-conditions** or **post-conditions** on a function
##### Decorator pattern mock-code example
```python
from sklearn import metrics
from abc import ABC, abstractmethod

# --- Interface component --- #
class ModelEvaluator(ABC): # Explicitly make it an Abstract Base Class
 """Base class for model evaluation."""

 @abstractmethod
 def evaluate(self, model, X_test, y_test):
 """Subclasses must implement 'evaluate' method."""
 pass 

# --- Concrete component --- #
class BasicEvaluator(ModelEvaluator):
 """Basic evaluator that just predicts and returns predictions."""

 def evaluate(self, model, X_test, y_test):
 y_pred = model.predict(X_test)
 return y_pred

# --- Basic Decorator --- #
class EvaluationDecorator(ModelEvaluator): # Inherits from abstract class
 """Base decorator for adding evaluation metrics."""

 def __init__(self, evaluator: ModelEvaluator):
 self.evaluator = evaluator

 def evaluate(self, model, X_test, y_test):
 # Perform base evaluation first
 y_pred = self.evaluator.evaluate(model, X_test, y_test)
 
 # Add decorated evaluation logic
 self._print_metric(y_test, y_pred)
 return y_pred

 @abstractmethod
 def _print_metric(self, y_true, y_pred):
 """Subclasses must implement '_print_metric' method."""
 pass

# --- Concrete Decorators ---
class AccuracyEvaluator(EvaluationDecorator):
 """Decorator to calculate and print accuracy."""

 def _print_metric(self, y_true, y_pred):
 accuracy = metrics.accuracy_score(y_true, y_pred)
 print(f"Accuracy: {accuracy:.4f}")

class PrecisionEvaluator(EvaluationDecorator):
 """Decorator to calculate and print precision."""

 def _print_metric(self, y_true, y_pred):
 precision = metrics.precision_score(y_true, y_pred)
 print(f"Precision: {precision:.4f}")

# Usage Example:
# Assume 'model', 'X_test', and 'y_test' are defined

basic_evaluator = BasicEvaluator()
accuracy_evaluator = AccuracyEvaluator(basic_evaluator)
full_evaluator = PrecisionEvaluator(accuracy_evaluator) # Chaining decorators

full_evaluator.evaluate(model, X_test, y_test) 
```
<!--SR:!2026-04-25,148,290-->