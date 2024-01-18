from Day_06 import char_count

def test_letter_char_count():
    """Given a short string and a letter, return a count of that letter's occurrences."""
    str = "banana"
    char = "a"

    result = char_count(str, char)
    assert result == 3