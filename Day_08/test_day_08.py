from Day_08 import letter_count

def test_word_count():
    """Given a single word string, return a dictionary containing a count of lowercase and uppercase letters."""
    str = "Python"
    result = letter_count(str)
    assert result == {"uppercase": 1, "lowercase": 5}

def test_sentence_count():
    """Given a sentence, return a dictionary containing a count of lowercase and uppercase letters."""
    str = "I love Python"
    result = letter_count(str)
    assert result == {"uppercase": 2, "lowercase": 9}