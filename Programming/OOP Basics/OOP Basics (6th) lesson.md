[\<previous](OOP%20Basics%20(5th)%20lesson%201.md)
**Codewords:** Magic Methods (\_\_repr\_\_, \_\_str\_\_, \_\_call\_\_)
- **Comparison Operators:**
- **__eq__(self, other):** Equality (==)
- **__ne__(self, other):** Inequality (!=)
- **__lt__(self, other):** Less than (<)
- **__le__(self, other):** Less than or equal to (<=)
- **__gt__(self, other):** Greater than (>)
- **__ge__(self, other):** Greater than or equal to (>=)
- **Container Emulation:**
- **__len__(self):** Returns the length of the object (used by len()).
- **__getitem__(self, key):** Allows access to elements using indexing (e.g., my_object[key]).
- **__setitem__(self, key, value):** Allows setting elements using indexing (e.g., my_object[key] = value).
- **__delitem__(self, key):** Allows deleting elements using indexing (e.g., del my_object[key]).
- **__contains__(self, item):** Checks for membership (used by the in operator).