# Exercise 20: Write a Python program that declares an integer variable B and assign it a value. 
# # It then displays a message indicating whether the value of B is positive or negative. We will consider 0 as positive.
# # If for example B = 1 the output will be 1 is positive. If for example B = -1 the output will be: -1 is negative.

Variable_B = int(-5)

if Variable_B < 0:
    print(f"{Variable_B} is negative.")
else:
    print(f"{Variable_B} is positive.")