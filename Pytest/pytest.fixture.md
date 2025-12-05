
This is the core building block of tests in pytest. It is a way to create reusable setup code.

Instead of writing the same setup logic (like "create a database connection" or "initialize the Agent") inside every single test function, you write it once in a fixture.
- Dependency Injection: When you see def test_full_flow(buyer_example, ...):, pytest automatically looks for a fixture named buyer_example, runs it, and passes the return value into your test function.
- Composability: Fixtures can use other fixtures. Notice def buyer_example(mock_buyer_sdk, ...)? This fixture is requesting the mock_buyer_sdk fixture before it runs itself.