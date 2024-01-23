from Day_11 import xtable
import pytest

def test_xtable_no_limit():
    """Given a number and no specified upper limit, return a list of products for that number multiplied from 0-12."""
    number = 12
    result = xtable(number)
    expected = [
        (0, 0), 
        (1, 12),
        (2, 24),
        (3, 36),
        (4, 48),
        (5, 60),
        (6, 72), 
        (7, 84),
        (8, 96),
        (9, 108),
        (10, 120), 
        (11, 132),
        (12, 144)
    ]
    assert result == expected

def test_xtable_w_up_limit():
    """Given a number and a specified upper limit, return a list of products for that number multiplied from 0-limit."""
    number = 10
    upper = 10
    result = xtable(number, upper)
    expected = [
        (0, 0),
        (1, 10),
        (2, 20),
        (3, 30), 
        (4, 40), 
        (5, 50), 
        (6, 60),
        (7, 70), 
        (8, 80),
        (9, 90), 
        (10, 100)
    ]
    assert result == expected

def test_xtable_w_low_limit():
    """Given a number and a specified lower limit, return a list of products for that number multiplied from lower-upper limit."""
    number = 10
    lower = 11
    upper = 20
    result = xtable(number, upper, lower)
    expected = [
        (11, 110),
        (12, 120),
        (13, 130),
        (14, 140),
        (15, 150), 
        (16, 160),
        (17, 170),
        (18, 180),
        (19, 190), 
        (20, 200)
    ]
    assert result == expected

def test_xtable_type_error():
    """Given an invalid input, return a TypeError with message 'Input must be integer'."""
    string = "oops"
    with pytest.raises(TypeError) as excinfo:
        xtable(string)
    assert str(excinfo.value) == 'Input must be an integer.'

def test_xtable_value_error():
    """Given an upper limit that is smaller than the lower limit, return an error."""
    number = 10
    lower = 20
    upper = 11
    with pytest.raises(ValueError) as excinfo:
        xtable(number, upper, lower)
    assert str(excinfo.value) == 'Upper limit must be larger than lower limit.'