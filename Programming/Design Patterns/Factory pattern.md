#🃏/programming
What is a **Factory** design pattern? When is it useful and how would you know if you will benefit from utilizng it? How is it different from the [[Strategy pattern]]? Provide some mock-code example of a class designed within a **Factory** paradigm.
?
**Factory** is a [[Creational patterns | creational]] desing pattern allows you to create similar objects, hiding the creation implementation details and providing an convinient interface for you. It includes three main elements, just like the [[Strategy pattern]]:
1. **Abstract Class** defines one single interface to share between child classes, so they indeed will have one shared type.
2. **Concrete Classes** defining concrete objects to create.
3. **Factory class** implementing the varying creation process.
> Note! The [[Strategy pattern]] is indeed very similar to the **Factory pattern**, but they do pursue two different main goals:
- **Strategy pattern** is used to vary some **single method behaviour** by providing him some **strategy** (class or some submethod). This is needed when you need to perform one **OPERATION** and vary implementation (e.g. do **PREPROCESSING** using GaussianSmoothing or Blurring..)
- **Factory pattern** is used to **CREATE** different objects, which could be used further in any way you would want, so you do not have a concrete **OPERATION** to perform right away, you are just willing to create some object with convinience.
<br>
You can benefit from using the **Factory pattern** if:
1. Your object creation logic is complex/conditional, and you want to hide **switch/if-else** logic inside your module.
2. Your object creation logic relies on some configuration files or environmental variables.
3. You want to distinguish the process of object creation and object usage inside your application.
------------------------------------------------------------
Factory pattern design example:
```python

class AbstractDocParser(ABC):
	@abstractmethod
	def parse(doc_path : Path) -> np.ndarray:
		pass

class ParserForPdf(AbstractDocParser):
	def parse(doc_path : Path) -> np.ndarray:
		return _parse_pdf(doc_path)

	def _parse_pdf(doc_path : Path) -> np.ndarray:
		# Some logic
		return ...

class ParserForWord(AbstractDocParser):
	def parse(doc_path : Path) -> np.ndarray:
		return _parse_word(doc_path)

	def _parse_word(doc_path : Path) -> np.ndarray:
		# Some logic
		return ...

class ParserFactory:
	@staticmethod 
	def create_parser(file_type: str) -> AbstractDocParser: 
	if file_type == 'pdf': 
		return ParserForPdf() 
	elif file_type == 'docx': 
		return ParserForWord() 
	else: 
		raise ValueError("Invalid file type")

class StrategyContextParse:
	@staticmethod
	def parse_file(parser: AbstractDocParser) -> np.ndarray:
		return parser.parse
```
In this example we actually have combined **Factory** and **Strategy** patterns, as they are often used together. Factory pattern handles conditional creation logic, and Strategy pattern is used to actually perform the parsing itself, utilizing creater preprocessors as strategies.
<!--SR:!2025-05-14,180,310-->