import pytest
from ops import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 5) == 2

def test_square():
    assert square(4) == 16

def test_cube():
    assert cube(3) == 27


def test_add():
    assert add(7, 7) == 14

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_divide_good(a, b, expected_result):
    assert divide(a, b) == expected_result

def test_zero_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
