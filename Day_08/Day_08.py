# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# def char_overview(str):
#     count = {"uppercase": 0, "lowercase": 0}

#     for char in str:
#         code = ord(char)
#         if code >= 65 and code <= 90:
#             count["uppercase"] += 1
#         elif code >= 97 and code <= 122:
#             count["lowercase"] += 1

#     return count

# OK, but what if I want more details, like:
# - how many numbers there are
# - how many spaces there are
# - how many additional characters there are
# BUT I don't want to see a category if it's 0.

def char_overview(str):
    count = {
        "uppercase": 0, 
        "lowercase": 0, 
        "number": 0, 
        "space": 0, 
        "other": 0
    }

    for char in str:
        code = ord(char)
        if code == 32:
            count["space"] += 1
        elif code >= 48 and code <= 57:
            count["number"] += 1
        elif code >= 65 and code <= 90:
            count["uppercase"] += 1
        elif code >= 97 and code <= 122:
            count["lowercase"] += 1
        else:
            count["other"] += 1
        
    for key in count.copy():
        if count[key] == 0:
            del count[key]

    if len(count) == 0:
        return None

    return count