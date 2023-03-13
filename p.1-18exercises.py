#Exercise 18: Write a program in Python that reads two numbers on the keyboard and 
# # say which is the largest and which is the smallest.

number_1 = input("Please enter first number: ")
number_2 = input("Please enter second number: ")

if number_1 < number_2:
    print(f"{number_1} is smaller than {number_2}")
else:
    print(f"{number_1} is greater than {number_2}")