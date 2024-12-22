#🃏/programming
What is a **Strategy** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **strategy** paradigm.
?
**Strategy** is a [[Behavioral patterns | behavioral]] that pattern allows you to change functions behavior dynamically by providing a "strategy" argument. It consists of 3 main parts:
1. **Context Class:** This class contains a reference to a Strategy class and delegates the actual algorithm to it.
2. **Strategy Interface:** And abstract class which defines a common interface for all supported algorithms.
3. **Concrete Strategies:** Implement the Strategy interface with different algorithms.
##### Why use Strategy pattern?
You can possibly benefit from using it if you find yourself in a sutiatuon when:
1. You have one shared task and many interchangable algorthims completing it in a different manner.
2. Your method has a lot of `if-else` or `switch` statements.
-----------------------------------------------------------
Strategy pattern design example:
```python

class AbstractPreprocessingStrategy(ABC):
	@abstractmethod
	def preprocess(np_image : np.ndarray) -> np.ndarray:
		pass
		
class PreprocessingStrategy1(AbstractPreprocessingStrategy):
	def preprocess(np_image : np.ndarray) -> np.ndarray:
		np_image = #some logic here
		return np_image

class PreprocessingStrategy2(AbstractPreprocessingStrategy):
	def preprocess(np_image : np.ndarray) -> np.ndarray:
		np_image = #some different logic here
		return np_image
		
class ContextClass:
	def __init__(self, selected_strategy : AbstractPreprocessingStrategy):
		self.strategy = selected_strategy

	def preprocess(np_image : np.ndarray) -> np.ndarray:
		return self.strategy.preprocess(np_image)
```
<!--SR:!2025-05-26,192,310-->


