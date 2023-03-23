# Write an algorithm and a sub-algorithm. Write two variables with the same name and the compiler does not show error.

def multi():
    number = 10
    number1 = 10
    print(number * number1)
multi()

def another_multi():
    number = 11
    number1 = 11
    print(number * number1)
    multi()
another_multi()
