from Day_01 import swap
# Function should accept two variables as arguments.

def test_num_swap():
    """Swap two varibles with numerical values."""
    var1 = 1
    var2 = 2

    assert var2, var1 == swap(var1, var2)

def test_str_swap():
    """Swap two variables with string values."""

    var1 = "foo"
    var2 = "bar"

    assert var2, var1 == swap(var1, var2)

def test_mix_swap():
    """Swap two variables where one has a string value and the other a numerical value."""
    var1 = 1
    var2 = "foo"

    assert var2, var1 == swap(var1, var2)

    