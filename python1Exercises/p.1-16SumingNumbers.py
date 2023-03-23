
#Exercise 16: Write a program in Python that reads an integer from the keyboard and makes the sum of the next 100 numbers, 
# # showing the result on screen.
user_number = input("Please enter a number: ")
count = 0
SUM = 0
next_number = (int(user_number) + 1)

while count < 100:
    for num in range (int(next_number), int(next_number + 100)):
        SUM = num + SUM
        count += 1

print(SUM)

#############################################################################################################################################

user_number = input("Please enter a number: ")
count = 0
sum_sum = 0
next_number = int(user_number)

while count < 100:
    next_number = next_number + 1
    sum_sum = next_number + sum_sum
    count += 1

print(sum_sum)
