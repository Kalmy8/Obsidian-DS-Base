- Are used to create some testing data, which will be different each time you call a test thus can show you some flaws in the testing suite
- **FactoryBoy** is an external library, which allows you to:
	- Mimick an arbitrary class behavior (all the methods) using class Meta:... mechanism
	- Override any attributes and assign some random values to them
		- In fact, FactoryBoy has a plenty of pre-defined datasets of mobile numbers, names, emails etc.
			- There are some community-created datasets as well
		- It also has all sort of random generators (date, choice, number etc.)
	- ![[Pasted image 20251205234641.png]]

### 1. Is there something built-in in Pytest?
No, `pytest` is just a test runner. It does not generate data.
- **Faker**: The standard library for generating random raw data (strings, emails, etc.).
- **FactoryBoy**: Wraps Faker to generate complex **Objects/Models**.
- **Hypothesis**: Advanced "Property-Based Testing" (generates edge cases automatically).

### 2. The "Non-Deterministic" Controversy
You are right: **Purely random tests are dangerous** because they are flaky (pass today, fail tomorrow).

#### Solution A: Seeding (The "Fixed Random" approach)
We use a **SEED** to make randomness deterministic.
- If you set `Faker.seed(42)`, it generates the *exact same* "random" sequence every time.
- If a test fails, you know the seed, so you can reproduce it.

#### Solution B: Parametrization (Your "100 objects" idea)
Instead of random generation, pytest suggests **Parametrization** for fixed datasets.

```python
# The "100 objects" approach (Deterministic)
@pytest.mark.parametrize("user_input, expected", [
    ("user1", True),
    ("user2", False),
    # ... 98 more cases ...
])
def test_users(user_input, expected):
    assert check_user(user_input) == expected
```

### Summary: When to use what?
| Approach                  | Tool                      | Use Case                                                                                             |
| :------------------------ | :------------------------ | :--------------------------------------------------------------------------------------------------- |
| **Fixed Data**            | `pytest.mark.parametrize` | Testing known edge cases (empty strings, nulls, exact logic).                                        |
| **Deterministic Random**  | `FactoryBoy` + `Seed`     | Populating huge databases where specific values don't matter (e.g., "just give me 50 active users"). |
| **True Random / Fuzzing** | `Hypothesis`              | Finding bugs you didn't think of. (e.g., "What if the username is 10MB long?").                      |