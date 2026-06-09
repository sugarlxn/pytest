import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

def test_user_name(user):
    assert user["name"] == "Alice"

def test_user_age(user):
    assert user["age"] == 30
