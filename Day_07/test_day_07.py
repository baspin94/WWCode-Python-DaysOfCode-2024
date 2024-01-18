from Day_07 import check_sign
import pytest

def test_check_int_sign():
    """Given an integer, return whether it is positive, negative, or zero."""
    number = 42
    result = check_sign(number)
    assert result == "Positive"

    number = -42
    result = check_sign(number)
    assert result == "Negative"

    number = 0
    result = check_sign(number)
    assert result == "Zero"

def test_check_float_sign():
    """Given a float, return whether it is positive, negative, or zero."""
    number = 23.19
    result = check_sign(number)
    assert result == "Positive"

    number = -867.5309
    result = check_sign(number)
    assert result == "Negative"

    number = 0.000000001
    result = check_sign(number)
    assert result == "Positive"

    number = -0.000000001
    result = check_sign(number)
    assert result == "Negative"

def test_error():
    """Given a non-numerical input, return a TypeError."""
    number = "Threeve"
    with pytest.raises(TypeError):
        result = check_sign(number)