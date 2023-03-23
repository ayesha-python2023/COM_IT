# Exercise 22: Make the program in Python such that given as a worker's salary, apply a 15% increase
#  if your salary is less than $ 1000 and 12% otherwise. Print the new salary of the worker.
# Fact: SUE (variable of real type that represents the salary of the worker).

SALARY = float(input("Please enter your salary amount:  "))

if 0 < SALARY < 1000:
    new_salary = SALARY * 0.15
    print(f"Your new salary is now {new_salary}.")
elif SALARY >= 1000:
    new_salary = SALARY * 0.12
    print(f"Your new salary is now {new_salary}.")
else:
    print("Please enter a valid amount.")