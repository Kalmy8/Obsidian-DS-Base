
## What is a Stub?

A **stub** is a minimal fake implementation that returns pre-defined responses. Unlike mocks, stubs don't track calls or verify interactions  they just "stand in" for a real component.

**Key difference from Mocks:**
- **Mock** = verify *behavior* (did you call X with Y arguments?)
- **Stub** = verify *state* (given this input, is the output correct?)

## When to Use Stubs Over Mocks

| Use Stubs When...                                        | Use Mocks When...                                |
| -------------------------------------------------------- | ------------------------------------------------ |
| You need a fake service for integration/BDD tests        | You need to verify specific method calls         |
| The dependency is complex (DB, external API)             | You're testing that code *interacts correctly*   |
| **You want tests decoupled from implementation details** | Implementation details matter (retries, caching) |
| Multiple tests need the same fake behavior               | Each test needs different call verification      |

### Rule of Thumb
- **Unit tests** - Mocks (verify interactions)
- **Integration/BDD tests** - Stubs (verify end-to-end behavior)

## Stub Examples

### 1. Simple Function Stub
```python
# Instead of mocking requests.get and verifying calls...
# Just create a stub that returns what you need:

def stub_get_user(user_id: int) -> dict:
    """Stub that always returns a valid user."""
    return {"id": user_id, "name": "Test User", "active": True}

# In test:
def test_user_greeting(monkeypatch):
    monkeypatch.setattr("myapp.api.get_user", stub_get_user)
    result = generate_greeting(user_id=42)
    assert result == "Hello, Test User!"
    # Notice: we don't check IF get_user was called  we check the RESULT
```

### 2. Stub Class (Fake Repository)
```python
class StubUserRepository:
    """In-memory fake that replaces a real database repository."""

    def __init__(self):
        self.users = {}

    def save(self, user: User) -> None:
        self.users[user.id] = user

    def get(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def delete(self, user_id: int) -> None:
        self.users.pop(user_id, None)

# In test:
def test_user_service_creates_user():
    repo = StubUserRepository()  # No database needed!
    service = UserService(repository=repo)

    service.create_user(name="Alice")

    # Verify STATE, not interactions:
    assert len(repo.users) == 1
    assert list(repo.users.values())[0].name == "Alice"
```

### 3. HTTP Stub Server (for BDD/Integration)
```python
# Using responses library to stub HTTP calls
import responses

@responses.activate
def test_payment_flow():
    # Stub the payment gateway
    responses.add(
        responses.POST,
        "https://api.stripe.com/v1/charges",
        json={"id": "ch_123", "status": "succeeded"},
        status=200
    )

    # Test the full flow  don't care HOW it calls Stripe
    result = process_payment(amount=100, card="tok_visa")
    assert result.success is True
```

### 4. Stub for BDD Step Definitions
```python
# features/steps/payment_steps.py
from behave import given, when, then

class StubPaymentGateway:
    """Fake payment service for BDD tests."""

    def __init__(self):
        self.should_succeed = True
        self.processed_payments = []

    def charge(self, amount: int, card: str) -> dict:
        self.processed_payments.append({"amount": amount, "card": card})
        if self.should_succeed:
            return {"status": "success", "id": "stub_123"}
        return {"status": "failed", "error": "Card declined"}

@given("the payment gateway is available")
def step_impl(context):
    context.payment_gateway = StubPaymentGateway()
    # Inject stub into the app
    context.app.payment_service = context.payment_gateway

@given("the payment gateway will decline cards")
def step_impl(context):
    context.payment_gateway.should_succeed = False

@then("a payment of ${amount} should be processed")
def step_impl(context, amount):
    payments = context.payment_gateway.processed_payments
    assert any(p["amount"] == int(amount) for p in payments)
```

## Stubs vs Mocks: Side-by-Side

```python
# ===== MOCK APPROACH (verify interactions) =====
def test_sends_welcome_email_mock():
    with patch("myapp.email.send") as mock_send:
        register_user("alice@example.com")

        # Verify HOW the code behaved:
        mock_send.assert_called_once_with(
            to="alice@example.com",
            subject="Welcome!",
            body=ANY
        )

# ===== STUB APPROACH (verify state) =====
class StubEmailService:
    def __init__(self):
        self.sent_emails = []

    def send(self, to, subject, body):
        self.sent_emails.append({"to": to, "subject": subject, "body": body})

def test_sends_welcome_email_stub():
    email_service = StubEmailService()
    register_user("alice@example.com", email_service=email_service)

    # Verify WHAT happened (state), not HOW:
    assert len(email_service.sent_emails) == 1
    assert email_service.sent_emails[0]["to"] == "alice@example.com"
```

## Why Stubs Make Better Integration Tests

1. **Less brittle**: Mocks break when implementation changes (different method signature, different call order). Stubs only care about end results.
2. **Reusable**: A `StubUserRepository` can be shared across hundreds of tests. Mock setups are usually per-test.
3. **Readable**: `StubPaymentGateway().should_succeed = False` is clearer than complex mock configurations.
4. **Closer to reality**: Stubs can maintain state (like a real DB), making tests more realistic than mocks that return canned values without context.

