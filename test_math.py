# This is a simple test file for testing the add function.

def add(a , b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("pytest: test_add ")

def test_fail():
    assert add(2, 2) == 5
    print("pytest: test_fail ")

