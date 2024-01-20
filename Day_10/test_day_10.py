from Day_10 import rm_duplicates
import pytest

def test_num_list():
    """Given a short list of numbers, return a list of unique values."""
    items = [1, 1, 1, 2, 3, 5, 5, 6, 6, 6, 6]
    result = rm_duplicates(items)
    assert len(result) == 5
    expected = [1, 2, 3, 5, 6]
    for item in expected:
        assert item in result
    
def test_str_list():
    """Given a short list of strings, return a list of unique values."""
    items = ["apple", "apple", "banana", "banana", "banana", "orange"]
    result = rm_duplicates(items)
    assert len(result) == 3
    expected = ["apple", "banana", "orange"]
    for item in expected:
        assert item in result

def test_mix_list():
    """Given a list of mixed data types, return a list of unique values."""
    items = [True, True, False, 7, 8, 8, "Duck", "Duck", "Goose"]
    result = rm_duplicates(items)
    expected = [True, False, 7, 8, "Duck", "Goose"]
    assert len(result) == len(expected)
    for item in expected:
        assert item in result