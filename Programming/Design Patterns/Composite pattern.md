#🃏/programming
What is a **Composite** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Composite** paradigm.
?
[Composite.mhtml](../../📁%20files/Composite.mhtml)
The **Composite pattern** is a [structural pattern](Structural%20patterns.md)  used to represent tree-like hierarchial structures within your code, allowing you to interact with the whole structure as with a single object. It is very useful for some complex calculations, which involve a lot of parent-child related objects. Some examples would be:
1. Opening a file/folder in a file system.
2. Running a DecisionTree ML algorithm.
3. Working with some hierarchical structures like Manager>Manager>Worker.
##### Composite pattern structure
![Pasted image 20240830114258.png](../../📁%20files/Pasted%20image%2020240830114258.png)
The pattern itself consists of **3 main parts**:
1. The **Component** interface (abstractclass), which is being shared by all of the tree members. It **defines common (shared) operations for both tree nodes and leaves**.
2. The **Leaf** interface, which do the actual work an **implement all the functionality defined in a "Component" abstract class**.
3. The **Node** interface, which usually **extends basic "Component" interface with some utilitiraty operations** like add, remove, getChildren, etc.
##### Composite pattern usage scenarios
You can benefit from using the pattern in following situations:
1. You have to implement tree-like/recursive structure.
2. You want client code to utilize some elementary and composite element uniformally.
##### Composite pattern mock-code example
```python
class Component(ABC):
	def sum_up(self):
		pass

class Box(Component):
	def __init__(self):
		self.children = []
		
	def add(self, child : Composite):
		self.children.append(child)
		
	def remove(self, child: Composite):
		self.children.remove(child)

	def sum_up(self):
		box_sum = 0
		for child in self.children:
			box_sum += child.sum_up()
		return box_sum

class Product(Component):
	def __init__(self, price : int):
		self.price = price
		
	def sum_up(self):
		return self.price

main_box = Box()
branch1 = Box()
branch1.add(Box())
branch1.add(Product(100))

branch2 = Box()
branch2.add(Product(50))
main_box.add(branch1)
main_box.add(branch2)

# Count sum
main_box.sum_up()

```
