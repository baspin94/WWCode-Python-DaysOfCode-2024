from Day_04 import list_sum
import pytest

def test_int_sum():
    """Given a short list of integers, return the sum of those elements."""
    elements = [1, 2, 3]
    result = list_sum(elements)
    assert result == 6

def test_float_sum():
    """Given a short list of floats, return the sum of those elements."""
    elements = [0.1, 0.2, 0.3]
    result = list_sum(elements)
    assert result == 0.6

def test_mix_sum():
    """Given a short list of integers and floats, return the sum of those elements."""
    elements = [1, 2.5, 3.14]
    result = list_sum(elements)
    assert result == 6.64

def test_neg_sum():
    """Given a list including negative numbers, return the sum of those elements."""
    elements = [-1, 2.5, 3.14]
    result = list_sum(elements)
    assert result == 4.64

    elements = [1, -2.5, -3.14]
    result = list_sum(elements)
    assert result == -4.64

def test_non_num_error():
    """Given a list that includes non-numerical elements, raise a TypeError."""
    elements = ["apple", 1, 2]
    with pytest.raises(TypeError):
        list_sum(elements)