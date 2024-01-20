# Day 09
## Today's Challenge
Write a program to check if a number is even or odd.

## Notes
The code itself was relatively straightforward to write. As for the tests: with the way I've tested for error handling in the other challenges so far, the test passes even before I've written the corresponding code, because a general TypeError was returned. I wanted to find a way to check that my custom message is the one getting raised when the error occurs. 

I did some research and found a very helpful resource (other than the Pytest docs) that I will definitely be reviewing in more detail as I continue building my unit testing skills: [Pytest with Eric](https://pytest-with-eric.com/), in particular the post, ["How To Test Python Exception Handling Using Pytest Assert (A Simple Guide)"](https://pytest-with-eric.com/introduction/pytest-assert-exception/#Understanding-Exception-Testing), which provided several examples of how to check for specific exceptions and messages.

With the way I was writing my tests before, all I was doing was a basic check that a `TypeError` exception was being raised.

```python
def odd_or_even(integer):
    if integer % 2 == 0:
        return "Even"
    else:
        return "Odd"

def test_error():
    """Given an invalid input, return a TypeError."""
    string = "banana"
    with pytest.raises(TypeError):
        odd_or_even(string)
```
This worked fine, but when I ran the code myself using a string as an input, this was the message I received:
`TypeError: not all arguments converted during string formatting`

This does not provide a user with a clear reason why the code failed. I wanted to make it clearer what needs to change, with a message, "Input must be an integer."

From reviewing Eric's tutorial, I determined that in addition to the code I wrote above, I would need to capture the exception output in an object, `excinfo` (you could alias this object as anything you want, but this is how it is done in the official Pytest docs, too). That object has an attribute, value, which contains the error message. We'll convert that to a string to check it against our desired message.

```python
def test_error():
    """Given an invalid input, return a specific TypeError."""
    string = "banana"
    with pytest.raises(TypeError) as excinfo:
        odd_or_even(string)
    assert str(excinfo.value) == "Input must be an integer."
```
Now our test throws an error:
```
AssertionError: assert 'not all argu...ng formatting' == 'Input must be an integer.'
E         - Input must be an integer.
E         + not all arguments converted during string formatting
```
And now we can get that test to pass:
```python

def odd_or_even(integer):
    
    if type(integer) is not int:
        raise TypeError("Input must be an integer.")
    
    if integer % 2 == 0:
        return "Even"
    
    else:
        return "Odd"
```

## Helpful Resources
- [Pytest with Eric—"How To Test Python Exception Handling Using Pytest Assert (A Simple Guide)"](https://pytest-with-eric.com/introduction/pytest-assert-exception/#Understanding-Exception-Testing)
- [Pytest Docs—How to write and report assertions in tests](https://docs.pytest.org/en/7.1.x/how-to/assert.html?highlight=excinfo)