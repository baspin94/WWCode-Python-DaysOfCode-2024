# Challenge: Create a program that swaps the values of two variables.

def swap(a, b):
    a, b = b, a
    return a,b

var1 = True
var2 = False

print("Var1 after function:", var1)
print("Var2 after function:", var2)

var1, var2 = swap(var1, var2)

print("Var1 after function:", var1)
print("Var2 after function:", var2)