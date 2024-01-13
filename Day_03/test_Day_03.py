from Day_03 import count_vowels

def test_single_word():
    """Count how many vowels are in a single word."""
    word = "foo"
    result = count_vowels(word)
    assert result == 2

    word = "application"
    result = count_vowels(word)
    assert result == 5

    word = "system"
    result = count_vowels(word)
    assert result == 2

def test_y_option():
    """Exclude 'y' from count if specified."""

    word = "system"
    result = count_vowels(word, False)
    assert result == 1

def test_multiple_word_string():
    """Count how many vowels are in a multiple word string."""

    phrase = "I think Python is really cool!"
    result = count_vowels(phrase)
    assert result == 10

