---
type: note
status: done
tags: ['tech/python']
sources:
- "[[Refactoring Guru - Design Patterns]]"
authors:
-
---

#🃏/semantic/design-patterns #🃏/source/refactoring-guru/design-patterns

What is a **Prototype** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Prototype** paradigm.
?
The **Prototype** desing pattern allows you to create some class instances by using no common initialization techniques, but instead by copying from some base (prototype) instance. This might be useful if:
1. Going through class **\__init\__** routine is computationally expensive or time-consuming.
2. You have a lot of slighlty different typical objects in your application. In that case, copying will prevent you from **extensive subclassing**, when you want to avoid creating a large hierarchy of classes to represent slight variations of objects.
3. **Complex Object Configurations**: When objects are complex and their initial setup involves many configurations or dependencies, it might be easier to clone a pre-configured prototype rather than recreate it.
------------------------------------------------------------
Prototype desing pattern example:
```python
from copy import deepcopy

class Monster:
 def __init__(self, name, health, attack):
 self.name = name
 self.health = health
 self.attack = attack

 def __str__(self):
 return f"{self.name} (Health: {self.health}, Attack: {self.attack})"

# Create prototype monsters
prototype_monsters = {
 "goblin": Monster("Goblin", 20, 5),
 "troll": Monster("Troll", 50, 10),
 "dragon": Monster("Dragon", 100, 20),
}

# Function to spawn a monster from a prototype
def spawn_monster(monster_type):
 prototype = prototype_monsters.get(monster_type)
 if prototype:
 return deepcopy(prototype) # Create a deep copy of the prototype
 else:
 raise ValueError(f"Invalid monster type: {monster_type}")

# Usage
goblin1 = spawn_monster("goblin")
goblin2 = spawn_monster("goblin")

print(goblin1) # Output: Goblin (Health: 20, Attack: 5)
print(goblin2) # Output: Goblin (Health: 20, Attack: 5)
```
<!--SR:!2026-07-20,365,350-->

## Practical tasks:

1. **Game NPC Spawner**
 - Define a `NPC` class with `health`, `attack`, and `ai_behavior`.
 - Use a prototype registry to clone pre-configured NPCs (e.g., "Archer", "Mage") instead of reinitializing.