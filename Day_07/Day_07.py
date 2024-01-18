# Write a program to check if a number is positive, negative, or zero.
def check_sign(number):
    
    if type(number) is not int and type(number) is not float:
        raise TypeError("Input must be an integer or decimal/float.")
    
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"