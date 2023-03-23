# Exercise 21: Make a program in Python such that given as data the enrolment and 5 grades of a student; Print the enrolment, 
# the average and the word "approved" if the student has an average greater than or equal to 6, and the word "not approved" otherwise.
# Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that represents the student's enrolment.
# CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type variables representing the student's 5 grades.

enrolment = "MAT"
Grade_list = []
n = 1

while n < 6:
    grades = int(input(f"Please enter your {n} grade : "))
    Grade_list.append(grades)
    n += 1 

average_grade = sum(Grade_list) / len(Grade_list)

if average_grade >= 6:
    print(f"{enrolment} has an average garde {average_grade} and he is approved.")

else:
    print(f"{enrolment} has an average garde {average_grade} and he is not approved.")