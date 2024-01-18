# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def letter_count(str):
    count = {"uppercase": 0, "lowercase": 0}

    for char in str:
        code = ord(char)
        if code >= 65 and code <= 90:
            count["uppercase"] += 1
        elif code >= 97 and code <= 122:
            count["lowercase"] += 1

    return count

