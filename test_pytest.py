from calc import add, multiply, power


def test_add():
    assert add(1, 1) == 2
    assert add(-3, 1) == -2


def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(-3, 1) == -3
    assert multiply(-1,-3)  == 3


def test_power():
    assert power(1, 1) == 1
    assert power(2, 4) == 16
