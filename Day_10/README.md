# Day 10
## Today's Challenge
Write a program to remove duplicates from a list.

## Notes
Here was my initial code:
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
I thought I could be clever and just convert all these to set to remove the duplicates, and then back into a list. But because sets are unordered, I can't guarantee what order the unique values will be in for the purpose of the test.

If the order of the output does not matter for the purposes of the function, then I just need to approach the tests differently. In this case, instead of checking for an exact list, I want to check that the number of items is what I expect and each of the values I expect are included somewhere.

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
Now, if we did want to preserve the original order of the list, we'll need to use a different approach with the code, and should update the tests accordingly to check for the precise list we're expecting.

```python
def rm_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

def test_str_list():
    """Given a short list of strings, return a list of unique values."""
    items = ["apple", "apple", "banana", "banana", "banana", "orange"]
    result = rm_duplicates(items)
    expected = ["apple", "banana", "orange"]
    assert result == expected
```
## Helpful Resources
- [W3 Schools—Python Sets](https://www.w3schools.com/python/python_sets.asp)
