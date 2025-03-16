#🃏/design_patterns
What is a **Chain of Responsibility pattern** design pattern? When is it useful and how would you know if you will benefit from utilizng it? What are the concrete usage examples of CoR pattern applied to data science sphere? How CoR is different from stacking a few [decorators](Decorator%20pattern.md)?  Provide some mock-code example of a class designed within a **Chain of Responsibility pattern** paradigm.
?
[Chain of Responsibility.mhtml](../../📁%20files/Chain%20of%20Responsibility.mhtml)
The **Chain pattern** is a [behavioral pattern](Behavioral%20patterns.md) used to define some multi-stage processing pipeline, where each handler can either process the request and/or pass it further, truncate the request if it is invalid. Constructed chain can be called from whatever node you need, and all of the handlers do share the common interface for client's usage.
The CoR pattern is a relatively popular among data scienctists as it deals **great with handling pipelines**:
1. Data Validation and Preprocessing (MissingValueHandler -> ScalingHandler -> EncodingHandler -> NormalizationHandler)
2. Model evaluation (AccuracyHandler -> PrecisionHandler -> RecallHandler -> F1ScoreHandler -> AUCRocHandler)
3. Model hyperparameter tuning (GridSearchHandler -> RandomSearchHandler -> BayesianOptimizationHandler)
4. Feature selection (VarianceThresholdHandler -> RFEHandler -> LassoHandler.)
5. Model stacking (BaseModel1Handler -> BaseModel2Handler -> MetaModelHandler.)
##### Chain structure
![Pasted image 20240903093940.png](Pasted%20image%2020240903093940.png)
The pattern itself consists of **3 main parts**:
1. **Handler interface (ABC):** abstract class, which defines only methods which are shared among all the handlers and being called in a chain (like `process()` method).
2. **BaseHandler anstract class :** a base **Handler interface \[1] subclass** extends it with the method responsible for handlers chaining. It can be an explicit method like `set_next(next_node: Handler)` or it can be implemented via initalization like `__init__(self, next_node: Handler)`. It also **contains all the methods for request redirection**: so methods to truncate, send further or process the request.
> Note: First 2 parts can usually be united together to some BaseHandler abstractclass, containing both the interface and the chaining methods.
3. **Concrete handlers classes:** **BaseHandler \[2] sublcasses** which hold all the implementation details for methods defined in BaseHandler.
##### Chain of Responsibility difference from Decorator pattern.
The CoR handlers can execute arbitrary operations independently of each other. They can also stop passing the request further at any point. On the other hand, various [Decorators](Decorator%20pattern.md) can extend the object’s behavior while keeping it consistent with the base interface. In addition, decorators aren’t allowed to break the flow of the request.
##### Chain of Responsibility usage scenarios
You can benefit from using the pattern in following situations:
1. It’s essential to execute several handlers in a particular order (you are dealing with **a pipeline**).
2. You want to allow dynamic changes in the processing of requests by adding or removing handlers.
3. When the handler for a request might need to change at runtime.
##### Chain of Responsibility pattern mock-code example
```python
class BaseHandler(ABC):
	def __init__(self, next_handler : BaseHandler):
		self.next_handler = next_handler
		
	@abstractmethod 
	def process(self, np_image: np.array) -> np.array:
		pass

	@abstractmethod
	def send_further(self):
		pass

	@abstractmethod 
	def truncate(self):
		pass

class ConvertGray:
	def process(self, np_image : np.array):
		image = self.make_gray(np_image)
		if self.next_handler:
			image = self.next_handler.process(image)
		return image

	def make_gray(np_image: np.array) -> np.array:
		...
```
<!--SR:!2025-04-16,152,310-->