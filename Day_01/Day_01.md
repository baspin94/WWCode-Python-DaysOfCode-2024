# Helpful Resources
## Challenge Code
- [Geeks4Geeks - Python Functions](https://www.geeksforgeeks.org/python-functions/?ref=lbp): clued me in that when you pass pre-defined variables into a function, it breaks the reference; whatever you do to those variables inside the function does not affect the variables outside of it.

- [StackOverflow - Is there a standardized method to swap two variables in Python?](https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python): The "tuple swap" (a, b = b, a) is the most straightforward way to switch the values of two variables.

- [OReilly - Swapping Values Without Using a Temporary Variable](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s02.html) refers to the above-mentioned "tuple swap" method as "tuple packing and unpacking". I also didn't realize that the parentheses around a tuple aren't usually necessary (other than for easier readability) unless their meaning could be misinterpreted (i.e. in a function call).

## Testing
- [StackOverflow - Use docstrings to list tests in py.test](https://stackoverflow.com/questions/28898919/use-docstrings-to-list-tests-in-py-test): provided configuration needed in `conftest.py` to display docstrings in pytest output.