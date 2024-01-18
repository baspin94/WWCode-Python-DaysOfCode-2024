# Day 04
## Today's Challenge
Write a program to find the sum of all elements in a list.

## Commentary
The most basic implementation of this challenge was straightforward, assuming a smaller list containing only integers.

Starting with writing the first test:
```python
from Day_04 import list_sum

def test_int_sum():
    """Given a short list of integers, return the sum of those elements."""
    elements = [1, 2, 3]
    result = list_sum(elements)
    assert result == 6
```
And then the code to make that test pass:
```python
def list_sum(elements):
    sum = 0
    for number in elements:
        sum += number
    return sum
```
Where this got tricky was when I added floats to the mix.

I added this test:
```python
def test_float_sum():
    """Given a short list of floats, return the sum of those elements."""
    elements = [0.1, 0.2, 0.3]
    result = list_sum(elements)
    assert result == 0.6
```
Which immediately failed with the following output:
```
FAILED module Given a short list of floats, return the sum of those elements. - assert 0.6000000000000001 == 0.6
```
This led me down a rabbit hole to figure out what was happening, which turned up this tutorial from the Python documentation, [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html). This is a nuance related to how floating-point numbers are represented by computers. As humans, we typically calculate decimal fractions using base 10 notation, but computers calculate using base 2 (binary). If you're curious about what the difference is between the two, this [tutorial on Binary Representation](https://bjc.edc.org/June2017/bjc-r/cur/programming/4-internet/1-number-representation/1-binary.html?topic=nyc_bjc%2F4-internet.topic&course=bjc4nyc.html&novideo&noassignment#:~:text=In%20base%2010%2C%20there%20are,the%20place%20to%20its%20right.) from University of California, Berkeley provides a good primer. 

To cut a long story short, the nice, relatively short value we're used to seeing when calculating decimals is often being rounded, but the value stored in memory is often many decimal places longer. To resolve this, I updated the code to return a manually rounded result, adding an optional parameter to specify how many decimal places to round to (which defaults to 2).
```python
def list_sum(elements, decimal_places=2):
    sum = 0
    for number in elements:
        sum += number
    return round(sum, decimal_places)
```
This also worked to pass the next two tests:
```python
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
```
To wrap this up, I added a test for exception handling:
```python
def test_non_num_error():
    """Given a list that includes non-numerical elements, raise a TypeError."""
    elements = ["apple", 1, 2]
    with pytest.raises(TypeError):
        list_sum(elements)
```
Then added a check of each element's type that will raise a `TypeError` if it fails.
```python
def list_sum(elements, decimal_places=2):
    sum = 0
    for number in elements:
        if not type(number) is int and not type(number) is float:
            raise TypeError("List elements must be integers or floats.")
        else: 
            sum += number
    return round(sum, decimal_places)
```

## Helpful Resources
- [Python Docs—Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [w3 Schools—Python raise Keyword](https://www.w3schools.com/python/ref_keyword_raise.asp)
- [Pytest Docs—Assertions about expected exceptions](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions)