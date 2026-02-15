"""
Task1. Write a function that returns the largest number of two numbers
(use DocStrings documentation strings in the function).
"""
def largest_numer(number1: float = 0,number2: float = 0):
    """
    Check whith is the largest number of two numbers.

    Parameters:
        number1/number2 (float or int): Numbers to check.
    
    Returns:
        Return the largest number of the 2 params, return None if equal.
    """
    if(number1 > number2):
        return number1
    elif(number2 > number1):
        return number2
    else:
        return None
    
# Test:
print(largest_numer())
print(largest_numer(1,1))
print(largest_numer(7,2))
print(largest_numer(18.2,3))