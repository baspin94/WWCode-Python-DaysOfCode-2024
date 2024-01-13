# Commentary
I'm planning to use this Python coding challenge as a way to also get some practice with writing unit tests with Pyunit, reinforcing some of the concepts I picked up in the [Introduction to Test and Behavior Driven Development](https://www.coursera.org/learn/test-and-behavior-driven-development-tdd-bdd/) course I took last year.

On the surface, this seemed to be a pretty straightforward task: "Create a program that swaps the values of two variables." However, this ended up testing and expanding my understanding of how variables interact within functions, not to mention the usefulness of tuples.

I started out by writing a basic test:
```python
from Day_01 import swap
# Function should accept two variables as arguments.
# Run `pytest -v` from command line for verbose output.

def test_num_swap():
    """Swap two varibles with numerical values."""
    var1 = 1
    var2 = 2

    swap(var1, var2)

    assert var1 = 2
    assert var2 = 1
```
Then I wrote the code that I thought would make that test pass easily:
```python
def swap(a, b):
    temp = a
    a = b
    b = temp
```
I figured that I could call my `swap` function on two pre-defined variables and switch them in place with the help of a temporary variable. However, that turned out to not be a case. Here was my test output:
```
FAILED test_Day_01.py::test_swap - assert 1 == 2
```
Even though I'd called the `swap` function on `var1` and `var2`, their values were still coming out the same afterwards. I did some debugging to check whether the function was working at all, and it was doing exactly as intended within the context of the function.

Input:
```python
def swap(a, b):
    print("Var1 in function before swap:", a)
    temp = a
    a = b
    b = temp
    print("Var1 in function after swap:", a)

var1 = 1
var2 = 2

print("Var1 before function:", var1)
swap(var1, var2)
print("Var1 after function:", var1)
```
Output:
```
Var1 before function: 1
Var1 in function before swap: 1
Var1 in function after swap: 2
Var1 after function: 1
```
Why wasn't this change carrying through? To make a long story short, that change was happening to a different variable. That is, `Var1` inside the function and `Var1` outside the function are two different references. The Geeks4Geeks and RealPython articles I describe in the 'Resources' section go into more detail about why that is. To get around this, what I ended up doing was returning a tuple with the new values.

Here's how I rewrote the test:
```python
def test_num_swap():
    """Swap two varibles with numerical values."""
    var1 = 1
    var2 = 2

    assert var2, var1 == swap(var1, var2)
```

And here's how I rewrote the code to pass the test:
```python
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
```
In fact, I didn't even need the temporary variable, thanks to Python's automatic tuple packing and unpacking that I learned about in this O'Reilly article, [Swapping Values Without Using a Temporary Variable](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s02.html).

```python
def swap(a, b):
    a, b = b, a
    return a,b
```
Tuple packing and unpacking streamline the actual swap and, if you wanted to take advantage of these results after the function executes, the reassignment of values.

```python
def swap(a, b):
    a, b = b, a
    return a,b

var1 = 1
var2 = 2

print("Var1 after function:", var1)
print("Var2 after function:", var2)

var1, var2 = swap(var1, var2)

print("Var1 after function:", var1)
print("Var2 after function:", var2)
```
Output:
```
Var1 after function: 1
Var2 after function: 2
Var1 after function: 2
Var2 after function: 1
```
Now, let's make sure this works for all data types, including mixed data types. Here are the additional tests I wrote for that purpose:
```python
def test_str_swap():
    """Swap two variables with string values."""

    var1 = "foo"
    var2 = "bar"

    assert var2, var1 == swap(var1, var2)

def test_bool_swap():
    """Swap two variables with boolean values."""
    var1 = True
    var2 = False

    assert var2, var1 == swap(var1, var2)

def test_mix_swap():
    """Swap two variables with mixed data types."""
    var1 = 1
    var2 = "foo"

    assert var2, var1 == swap(var1, var2)

    var1 = True
    var2 = "foo"

    assert var2, var1 == swap(var1, var2)
```
And here are the results:
```
E       AssertionError: False
E       assert False

test_Day_01.py:25: AssertionError
FAILED module Swap two variables with boolean values. - AssertionError: False
```
Hmm, why aren't the booleans working? 

Debugging my code, it seems like the code works as intended.
```
Var1 after function: True
Var2 after function: False
Var1 after function: False
Var2 after function: True
```
In this case, it was an issue with the test itself, or rather, how I represented the tuple on the left side of the assertion. This is a case where the parentheses around the tuple are necessary, because they caused pytest to misinterpret what the assertion was evaluating for ("assert false" as opposed to "assert"). Changing this line got all the tests passing.
```python
def test_bool_swap():
    ...
    assert (var2, var1) == swap(var1, var2)
```

# Helpful Resources
## Challenge Code
- [Geeks4Geeks - Python Functions](https://www.geeksforgeeks.org/python-functions/?ref=lbp#:~:text=Pass%20by%20Reference%20and%20Pass%20by%20Value): This article first clued me in that when you pass pre-defined variables into a function, it breaks the reference; whatever you do to those variables inside the function does not affect the variables outside of it.

- [Real Python - Pass by Reference in Python: Background and Best Practices](https://realpython.com/python-pass-by-reference/): This article provides a deep dive (with helpful examples, and some comparisons to C#) detailing how Python passes arguments by **assignment** as opposed to reference or value, and best practices for modifying your code for the desired results.

- [StackOverflow - Is there a standardized method to swap two variables in Python?](https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python): The "tuple swap" (a, b = b, a) is the most straightforward way to switch the values of two variables.

- [OReilly - Swapping Values Without Using a Temporary Variable](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s02.html): This article refers to the above-mentioned "tuple swap" method as "tuple packing and unpacking". I also didn't realize that the parentheses around a tuple aren't usually necessary (other than for easier readability) unless their meaning could be misinterpreted (i.e. in a function call).

## Testing
- [StackOverflow - Use docstrings to list tests in py.test](https://stackoverflow.com/questions/28898919/use-docstrings-to-list-tests-in-py-test): This post provided configuration needed in `conftest.py` to display docstrings in pytest output.