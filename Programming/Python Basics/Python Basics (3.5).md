---
type: note
status: done
tags: ['tech/python']
sources:
-
- "[[Python Basics Course]]"
authors:
-
---

#🃏/semantic/python #🃏/source/python-basics-course

**Codewords:** Logical Operators, Truthiness, Falsiness

### Logical Operators: `and`, `or`, `not`

Logical operators are used to combine conditional statements.

#### Truthiness and Falsiness
In Python, various values are considered "false'ish" when evaluated in a boolean context (e.g., in `if` statements or with logical operators). These include:
- Numeric zero (`0`, `0.0`, `0j`)
- Empty sequences (`''`, `()`, `[]`)
- Empty mappings (`{}`)
- `None`
- `False`

All other values are generally considered "truthy".

#### `and` Operator
The `and` operator returns `True` if both operands are `True`. Otherwise, it returns `False`.
It also exhibits "short-circuiting" behavior: if the first operand is falsy, the second operand is not evaluated.

```python
# Example 1: Both conditions are True
age = 25
is_student = True
print(age > 18 and is_student) # Output: True

# Example 2: One condition is False (short-circuited)
temperature = 15
is_sunny = False
print(temperature > 20 and is_sunny) # Output: False
```

#### `or` Operator
The `or` operator returns `True` if at least one of the operands is `True`. It only returns `False` if both operands are `False`.
It also exhibits "short-circuiting" behavior: if the first operand is truthy, the second operand is not evaluated.

```python
# Example 1: One condition is True
has_license = True
has_car = False
print(has_license or has_car) # Output: True

# Example 2: Both conditions are False
is_hungry = False
is_thirsty = False
print(is_hungry or is_thirsty) # Output: False
```

#### `not` Operator
The `not` operator negates the boolean value of its operand. If the operand is `True`, `not` makes it `False`, and vice versa.

```python
# Example 1: Negating a True value
is_active = True
print(not is_active) # Output: False

# Example 2: Negating a False value
is_empty = False
print(not is_empty) # Output: True
```

#### Using `or` for Default Value Assignment (Common Idiom)

A common Python idiom uses the `or` operator to assign a default value to a variable if the original variable is "falsy". This works because `or` returns the first truthy value it encounters, or the last value if all are falsy. This is particularly useful for providing fallbacks for potentially empty or `None` values.

```python
# Example 1: Assigning a default list if user_input is None
user_input_list: list | None = None
actual_list = user_input_list or []
print(actual_list) # Output: []

user_input_list = ["item1", "item2"]
actual_list = user_input_list or []
print(actual_list) # Output: ['item1', 'item2']

# Example 2: Assigning a default string if user_name is an empty string
user_name = ""
display_name = user_name or "Guest"
print(display_name) # Output: Guest

user_name = "Alice"
display_name = user_name or "Guest"
print(display_name) # Output: Alice
```

**Problems (Logical Operators):**
1. Check if a number `num` is between 10 and 20 (inclusive) using `and`.
2. Determine if a person is eligible for a discount: they are either a student OR they are over 65 years old.
3. Check if a boolean variable `is_logged_in` is `False` using the `not` operator.
4. Combine conditions: Check if a user is an 'admin' AND their `status` is 'active', OR if their `role` is 'guest'.

## Review Questions

Evaluate the following expression: `(True and False) or (not True)`.
?
- `(False) or (False)` which is `False`.

Write a Python expression that checks if a variable `x` is greater than 5 AND less than 10.
?
```python
5 < x < 10
```

How could `or` operator be used to conditionally assing a value to a variable?
?
- variable = value1 or value2
- here `or` returns first value1 if it's True(-ish), otherwise value2