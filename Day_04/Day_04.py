# Write a program to find the sum of all elements in a list.

# def list_sum(elements):
#     sum = 0
#     for number in elements:
#         sum += number
#     return sum

# What if there is a mix of integers and floats in the list?
# def list_sum(elements, decimal_places=2):
#     sum = 0
#     for number in elements:
#         sum += number
#     return round(sum, decimal_places)

# What if there are non-numerical elements in the list?
def list_sum(elements, decimal_places=2):
    sum = 0
    for number in elements:
        if not type(number) is int and not type(number) is float:
            raise TypeError("List elements must be integers or floats.")
        else: 
            sum += number
    return round(sum, decimal_places)

# list_sum(["apple", 1, 2])