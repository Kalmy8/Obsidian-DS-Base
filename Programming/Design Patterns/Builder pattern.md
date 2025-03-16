#🃏/design_patterns
What is a **Builder** design pattern? When is it useful and how would you know if you will benefit from utilizng it? Provide some mock-code example of a class designed within a **Builder** paradigm.
?
A **Builder** desing pattern allows you to create complex objects usining chaining methods technique, which simplifies the process and makes the object creation process much more convinient, especially for comples classes with many optional attributes. The design pattern includes **2 main parts**:
1. A class itself, containing the **\__init\__** method and all the desired functional.
2. A **Builder** class, offering you a handy interface for class instances creation.
<br>
You can benefit from using the **Builder** pattern in following scenarios:
* Your object have many optional parameters, leading to telescoping constructors.
* You need to create different variations of the same object type.
* The construction process of the object is complex or involves a **specific order** of steps.
------------------------------------------------------------
```python
class House:
    def __init__(self, **kwargs):
        self.windows = kwargs.get('windows', 0)  # Default to 0 windows
        self.doors = kwargs.get('doors', 0)      # Default to 0 doors
        self.has_garden = kwargs.get('has_garden', False)
        self.has_garage = kwargs.get('has_garage', False)
        self.has_pool = kwargs.get('has_pool', False)

    def __str__(self):
        return (f"House with {self.windows} windows, {self.doors} doors, "
                f"{'a garden, ' if self.has_garden else ''}"
                f"{'a garage, ' if self.has_garage else ''}"
                f"{'a pool, ' if self.has_pool else ''}"
                f"and all the comforts of home.")

class HouseBuilder:
    def __init__(self):
        self._windows = 0
        self._doors = 0
        self._has_garden = False
        self._has_garage = False
        self._has_pool = False

    def set_windows(self, number: int):
        self._windows = number
        return self  # Return self to allow chaining

    def set_doors(self, number: int):
        self._doors = number
        return self  # Return self to allow chaining

    def add_garden(self):
        self._has_garden = True
        return self  # Return self to allow chaining

    def add_garage(self):
        self._has_garage = True
        return self  # Return self to allow chaining

    def add_pool(self):
        self._has_pool = True
        return self  # Return self to allow chaining

    def build(self) -> House:
        return House(self._windows, self._doors, self._has_garden, self._has_garage, self._has_pool)

# Usage example
builder = HouseBuilder()
luxury_house = (builder
                .set_windows(10)
                .set_doors(5)
                .add_garden()
                .add_garage()
                .add_pool()
                .build())

simple_house = (builder
                .set_windows(4)
                .set_doors(2)
                .build())

print(luxury_house)  # House with 10 windows, 5 doors, a garden, a garage, a pool, and all the comforts of home.
print(simple_house)  # House with 4 windows, 2 doors, and all the comforts of home.

```
<!--SR:!2026-10-03,566,330-->

## Practical tasks:
1. **Pizza Builder**
    - Create a `Pizza` class with properties: `size` (str), `crust_type` (str), `toppings` (list).
    - Implement a `PizzaBuilder` with methods like `set_size()`, `set_crust()`, `add_topping()`, and `build()`.
    - Allow chaining: `PizzaBuilder().set_size("Large").set_crust("Thin").add_topping("Mushrooms").build()`.