[Почему здравый смысл важнее паттернов, а Active Record не так уж и плох / Хабр](https://habr.com/ru/companies/domclick/articles/515560/)

"""
#TODO
Active Record:
- Logic resides on the model class (e.g. AgentResponse.log_response).
- Pros: Simple, less code for basic CRUD, familiar to Django/Rails users.
- Cons: Violates SRP (mixes data & behavior), harder to test (requires mocking model/DB), tight coupling.

Repository Pattern:
- Separate class/layer for DB operations (e.g. AgentResponseRepository).
- Pros: Separation of concerns, easier to test (mock repository interface), flexible (swap storage backends).
- Cons: More boilerplate code.
"""