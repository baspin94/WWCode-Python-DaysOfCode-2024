# Write a program to print the multiplication table of a given number.
# Input: Number to base table off of, optional upper limit of table (default to 12)

def xtable(number, upper_limit = 12):
    if type(number) is not int:
        raise TypeError('Input must be an integer.')

    table = []
    for val in range(upper_limit + 1):
        product = number * val
        table.append(product)
    return table

# What if we want it to look like an actual table?