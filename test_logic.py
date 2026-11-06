from logic import greet, add


def test_greet():
    assert greet("Muizur") == "Hello Muizur"


def test_add():
    assert add(5, 3) == 8