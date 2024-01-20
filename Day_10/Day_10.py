# Write a program to remove duplicates from a list.

# Set Method (Does Not Preserve Order)
# def rm_duplicates(items):
#     return list(set(items))

# Iteration Method (Preserves Order)
def rm_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen