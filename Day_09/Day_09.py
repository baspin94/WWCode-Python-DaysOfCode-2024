# Write a program to check if a number is even or odd.
# Should accept an integer as input.

def odd_or_even(integer):
    
    if type(integer) is not int:
        raise TypeError("Input must be an integer.")
    
    if integer % 2 == 0:
        return "Even"
    
    else:
        return "Odd"