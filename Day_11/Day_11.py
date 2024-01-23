# Write a program to print the multiplication table of a given number.
# Input: Number to base table off of, optional upper limit of table (default to 12)
# What if we want to specify a lower limit as well?
# What if we want it to look like an actual table?

from tabulate import tabulate

def xtable(number, upper_limit = 12, lower_limit = 0):
    if type(number) is not int:
        raise TypeError('Input must be an integer.')
    if lower_limit >= upper_limit:
        raise ValueError('Upper limit must be larger than lower limit.')

    table = []
    for val in range(lower_limit, upper_limit + 1):
        product = number * val
        table.append((val, product))
    
    print(tabulate(table, headers = ["x", number], tablefmt="grid"))

    return table

xtable(12)
xtable(10, 10)
xtable(10, 20, 11)

