from Day_11 import xtable
import pytest

def test_xtable_no_limit():
    """Given a number and no specified upper limit, return a list of products for that number multiplied from 0-12."""
    number = 12
    result = xtable(number)
    assert result == [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]

def test_xtable_w_up_limit():
    """Given a number and a specified upper limit, return a list of products for that number multiplied from 0-limit."""
    number = 10
    upper = 10
    result = xtable(number, upper)
    assert result == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def test_xtable_w_low_limit():
    """Given a number and a specified lower limit, return a list of products for that number multiplied from lower-upper limit."""
    number = 10
    lower = 11
    upper = 20
    result = xtable(number, upper, lower)
    assert result == [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

def test_xtable_error():
    """Given an invalid input, return a TypeError with message 'Input must be integer'."""
    string = "oops"
    with pytest.raises(TypeError) as excinfo:
        xtable(string)
    assert str(excinfo.value) == 'Input must be an integer.'