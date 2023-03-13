# Exercise 21: Make a program in Python such that given as data the enrolment and 5 grades of a student; Print the enrolment, 
# the average and the word "approved" if the student has an average greater than or equal to 6, and the word "not approved" otherwise.
# Data: MAT, CAL1, CAL2, CAL3, CAL4, CAL5 Where: MAT is an integer variable that represents the student's enrolment.
# CAL1, CAL2, CAL3, CAL4 and CAL5 are real-type variables representing the student's 5 grades.

cal_1 = 9
cal_2 = 9
cal_3 = 3
cal_4 = 4
cal_5 = 5
AVERAGE = (cal_1 + cal_2 + cal_3 + cal_4 + cal_5) // 5

if AVERAGE < 6:
        print("MAT is not a approved.")
else:
        print("MAT is approved. ")