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

[Flyweight pattern](Flyweight%20pattern.md)

What is a **Flyweight** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Flyweight** paradigm.
?
[Flyweight pattern](Flyweight%20pattern.md)
The **Flyweight pattern** is a [structural pattern](Structural%20patterns.md) used to share some data between as much created class instances as possible, potentially saving a lot of RAM.
>Note: that this pattern is nowadays is not popular across the data science sphere, because most libraries do have their own optimisations for conscious memory-usage.
However, if you want to make use of it, you have to define:
- **Immutable repeating (intrisinc) state:** object data which stays the same across practically all of the created objects.
- **Mutable (extrisinc) state:** frequently changing object data which is unique across most part of the created objects.
---
The Flyweight pattern suggests that you **stop storing the extrinsic state inside the object**. Instead, you should pass this state to specific methods which rely on it. Only the intrinsic state stays within the object, letting you reuse it in different contexts. As a result, **you’d need fewer of objects since they only differ in the intrisinc state, which has much fewer variations** than the extrisinc. **This objects are called flyweights**, they are created and initalized only once and when re-used as much times as needed.
##### Flywheight pattern structure
![Pasted image 20240902214444.png](../../📁%20files/Pasted%20image%2020240902214444.png)
The pattern itself consists of **3 main parts**:
1. **Flywheight:** concrete class, which object are being intialized once with some heavy intrisinc data and re-used further. Some implementations are assume that this should be a [Dataclass](../Dataclass.md)
2. **Flywheight factory:** a [factory](Factory%20pattern.md) class, responsible for Flywheight objects creation and re-usage. It is likely to accept some intrisinc data as keys, and return an existing instance if it is already presented in RAM.
3. **Context class:** a class providing some interface for client and doing all the work. It's objects are being initialized based on some **Flywheight** object and adding some **extricing** data above. When this data is used alltogether by methods containing in context class.
##### Flyweight pattern usage scenarios
You can benefit from using the pattern in following situations:
1. You are running out of RAM executing your script, at the same time your application utilizes a big amount of similar objects, which attributes can be clearly separated to the extrisinc and intrisinct parts.
##### Flyweight pattern mock-code example
```python
from typing import Dict
from dataclasses import dataclass

# Flyweight class: stores the common, intrinsic state (as a simple data container)
@dataclass(frozen=True)
class TreeType:
 name: str
 color: str
 texture: str

# Flyweight Factory class: manages and shares Flyweight objects
class TreeTypeFactory:
 _tree_types: Dict[str, TreeType] = {}

 @classmethod
 def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
 key = f"{name}_{color}_{texture}"
 if key not in cls._tree_types:
 cls._tree_types[key] = TreeType(name, color, texture)
 print(f"Creating new TreeType: {key}")
 return cls._tree_types[key]

# Context class: stores extrinsic state, such as position
class Tree:
 def __init__(self, x: int, y: int, tree_type: TreeType):
 self.x = x
 self.y = y
 self.tree_type = tree_type # This refers to a shared Flyweight object

 def draw(self):
 """Draw the tree using its shared and unique state"""
 print(f"Drawing {self.tree_type.name} tree at ({self.x}, {self.y}) with color {self.tree_type.color} and texture {self.tree_type.texture}")

# Client code example
if __name__ == "__main__":
 trees = []
 factory = TreeTypeFactory()

 # Creating trees with shared types
 oak_type = factory.get_tree_type("Oak", "Green", "Rough")
 trees.append(Tree(10, 20, oak_type))

 pine_type = factory.get_tree_type("Pine", "Green", "Smooth")
 trees.append(Tree(30, 40, pine_type))

 another_oak_type = factory.get_tree_type("Oak", "Green", "Rough") # Reuse the shared Oak type
 trees.append(Tree(50, 60, another_oak_type))

 # Draw all trees
 for tree in trees:
 tree.draw()

```
<!--SR:!2026-01-16,327,290-->