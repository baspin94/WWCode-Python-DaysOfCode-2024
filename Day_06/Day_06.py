# Write a program to count the occurrences of a specific character in a string.

def char_count(str, char):
    count = 0

    for element in str:
        if element == char:
            count += 1
    
    return count