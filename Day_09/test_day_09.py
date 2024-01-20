from Day_09 import odd_or_even
import pytest

def test_odd_or_even_int():
    """Given an integer, return 'Even' or 'Odd'."""
    integer = 28
    result = odd_or_even(integer)
    assert result == "Even"

    integer = 33
    result = odd_or_even(integer)
    assert result == "Odd"

def test_zero():
    """Given an integer zero, return 'Even'."""
    integer = 28
    result = odd_or_even(integer)
    assert result == "Even"

def test_error():
    """Given an invalid input, return a specific TypeError."""
    string = "banana"
    with pytest.raises(TypeError) as excinfo:
        odd_or_even(string)
    assert str(excinfo.value) == "Input must be an integer."

# def test_error():
#     """Given an invalid input, return a specific TypeError."""
#     string = "banana"
#     with pytest.raises(TypeError):
#         odd_or_even(string)

