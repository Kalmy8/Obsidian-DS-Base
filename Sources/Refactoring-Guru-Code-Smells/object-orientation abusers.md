---
type: note
status: done
tags: ['tech/python']
sources:
-
authors:
-
---

#🃏/semantic/code-smells

All these smells are incomplete or incorrect application of object-oriented programming principles

What code smell falls into the "object-orientation" abusers, if:
- You have a complex `switch` operator or sequence of `if` statements.
- Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these circumstances, they’re empty.
- If a subclass uses only some of the methods and properties inherited from its parents
- Several classes perform identical functions but have different method names
?
- [[switch statements]]
- [[temporary field]][Temporary Field](https://refactoring.guru/smells/temporary-field)
- [[refused bequest]][Refused Bequest](https://refactoring.guru/smells/refused-bequest)
- [[alternative classes with different interfaces]][Alternative Classes with Different Interfaces](https://refactoring.guru/smells/alternative-classes-with-different-interfaces)

