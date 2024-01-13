# Create a program to calculate the area of a circle given its radius.
# This will return a decimal, which I will round to the nearest hundredth.
from math import pi

def area(radius):
    result = pi * radius**2
    return round(result, 2)

# NEXT: What if we wanted to set up user inputs?