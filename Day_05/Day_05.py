# Write a program to find the maximum and minimum values in a list.

def min_max(values):
    min = values[0]
    max = values[0]

    for value in values:
        if not type(value) is int and not type(value) is float:
            raise TypeError("Values must be integers or floats.")
        if value < min:
            min = value
        elif value > max:
            max = value
    
    return (min, max)