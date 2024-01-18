from Day_08 import char_overview

def test_word_count():
    """Given a single word string, return a dictionary containing a count of lowercase and uppercase letters."""
    str = "Python"
    result = char_overview(str)
    assert result == {"uppercase": 1, "lowercase": 5}

def test_sentence_count():
    """Given a sentence, return a dictionary containing a count of lowercase and uppercase letters."""
    str = "I love Python"
    result = char_overview(str)
    assert result == {"uppercase": 2, "lowercase": 9, "space": 2}

def test_empty():
    """Given an empty string, return None"""
    str = ""
    result = char_overview(str)
    assert result == None

def test_space_only():
    """Given a string containing only spaces, return a dictionary containing a count of spaces."""
    str = "     "
    result = char_overview(str)
    assert result == {"space": 5}

def test_numbers_only():
    """Given a string containing only numbers, return a dictionary containing a count of numbers."""
    str = "12345"
    result = char_overview(str)
    assert result == {"number": 5}

def test_other_only():
    """Given a string containing only special characters and punctuation, return a dictionary containing a count of other."""
    str = "!!*$%#@^()"
    result = char_overview(str)
    assert result == {"other": 10}

