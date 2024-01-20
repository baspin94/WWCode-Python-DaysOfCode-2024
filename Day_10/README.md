# Day 10
## Today's Challenge
Write a program to remove duplicates from a list.

## Notes
I thought I could be clever and convert all these to set to remove the duplicates, and then back into a list. But because sets are unordered, I can't guarantee what order the unique values will be in for the purpose of the test.

```python
def rm_duplicates(items):
    return list(set(items))

def test_str_list():
    """Given a short list of strings, return a list of unique values."""
    items = ["apple", "apple", "banana", "banana", "banana", "orange"]
    result = rm_duplicates(items)
    assert result == ["apple", "banana", "orange"]
```
```
FAILED module Given a short list of strings, return a list of unique values. - AssertionError: assert ['orange', 'banana', 'apple'] == ['apple', 'banana', 'orange']
```
Perhaps I could make the tests better by accounting for this. It doesn't matter what order the items are returned in, but I care that the duplicates are gone (the length of the list should be what I expect).

```python
def test_str_list():
    """Given a short list of strings, return a list of unique values."""
    items = ["apple", "apple", "banana", "banana", "banana", "orange"]
    result = rm_duplicates(items)
    assert len(result) == 3
```
I should also ensure that each of the unique values I'm expecting is present.
```python
def test_str_list():
    """Given a short list of strings, return a list of unique values."""
    items = ["apple", "apple", "banana", "banana", "banana", "orange"]
    result = rm_duplicates(items)
    expected = ["apple", "banana", "orange"]
    assert len(result) == len(expected)
    for item in expected:
        assert item in result
```
## Helpful Resources
- [W3 Schools—Python Sets](https://www.w3schools.com/python/python_sets.asp)
