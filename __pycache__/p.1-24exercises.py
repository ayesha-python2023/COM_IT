# 24 - Make_a_calculator.

input_1 = input("Please enter the first number: ")
operator = input("Please enter an operator")
input_2 = input("Please enter the second number: ")

result = eval(input_1 + operator + input_2)

print(f"{input_1} {operator} {input_2} is equal to {result}")
