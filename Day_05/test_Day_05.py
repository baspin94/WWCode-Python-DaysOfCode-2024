from Day_05 import min_max
import pytest

def test_int_min_max():
    """Given a short list of integers, return a tuple with the minimum and maximum values."""
    values = [7, 6, 10, 1, 2, 5]
    result = min_max(values)
    assert result == (1, 10)

def test_float_min_max():
    """Given a short list of floats, return a tuple with the minimum and maximum values."""
    values = [7.79645, 6.64, 10.987, 1.234, 2.345678, 5.02]
    result = min_max(values)
    assert result == (1.234, 10.987)

def test_mix_min_max():
    """Given a short list of ints and floats, return a tuple with the minimum and maximum values."""
    values = [7.79645, 6, 10.987, 1, 2.345678, 5.02]
    result = min_max(values)
    assert result == (1, 10.987)

def test_error():
    """Given a list including non-numerical elements, return a TypeError."""
    values = [1, 2, "buckle", "my", "shoe"]
    with pytest.raises(TypeError):
        min_max(values)