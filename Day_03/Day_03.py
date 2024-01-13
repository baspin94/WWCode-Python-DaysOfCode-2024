# Write a function to count the number of vowels in a given string.

# def count_vowels(string):
#     count = 0
#     string = string.lower()
#     vowels = ["a", "e", "i", "o", "u"]

#     for char in string:
#         if char in vowels:
#             count += 1

#     return count

# What if I want to give the option to include 'y' as a vowel?

def count_vowels(string, include_y=True):
    count = 0
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u", "y"]

    if not include_y:
        vowels.pop()

    for char in string:
        if char in vowels:
            count += 1

    return count

# NEXT: What if we wanted to set up user inputs?
# NEXT: What if we have to handle a really long string with a lot of whitespace and/or numbers?