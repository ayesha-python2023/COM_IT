"""
First we need to make a module that we can import to another python file:
"""

#def a function and return a value
def add(number_1: int, number_2: int) -> int:
    #add two numbers"
    sum_numbers = int(number_1) + int(number_2)
    print(sum_numbers)
    print(f"The sum of two given numbers is {sum_numbers}")
    return(sum_numbers)

