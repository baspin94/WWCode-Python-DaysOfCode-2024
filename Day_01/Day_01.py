# Challenge: Create a program that swaps the values of two variables.

def swap(a, b):
    # temp = a
    # a = b
    # b = temp
    # return a, b

    a, b = b, a
    return a,b

var1 = 1
var2 = 2

print(swap(var1, var2))