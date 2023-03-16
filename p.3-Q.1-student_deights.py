# Write a program that allows you to enter the height of 10 students, 
#then show the average height, and how many elements are above average, how many are below average.

#First step is to get the input for the students height data:
student_heights = []
height_tenStudents = 0

while height_tenStudents < 10:
    each_height = int(input("Please enter your height in inches: "))
    student_heights.append(each_height)
    height_tenStudents += 1

# Now we can calculate the average height by using a formula:
average_height = sum(student_heights) / len(student_heights)

print(f"Average height of the students is {average_height}.")

# This step is to find out how many students are above average, or below average:
above_average = 0
below_average = 0
equal_average_height = 0
i = 0
for student_heights[i] in student_heights:
    if student_heights[i] > average_height:
        above_average += 1
    
    elif student_heights[i] < average_height:
        below_average += 1
    else:
        equal_average_height += 1

print(f"{above_average} people are above average.")
print(f"{below_average} people are below average.")
print(f"{equal_average_height} people are average height.")

# now we can calculate the percentage: 
percent_of_above_average = above_average/len(student_heights)*100
print(f" {percent_of_above_average} of the class is above average." )

percentage_of_below_average = below_average/len(student_heights)*100
print(f" {percentage_of_below_average} of the class is above average." )

percentage_of_average_height = 100 - (percentage_of_below_average + percent_of_above_average)
print(f"{percentage_of_average_height} people are average height.")




