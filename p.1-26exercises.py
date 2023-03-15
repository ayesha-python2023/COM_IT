#
# Make a program that asks for the salary of N workers 
##(first you must ask how many workers there are) and 
##print the one with the highest salary.

workers = int(input("Please enter the number of workers"))
n = 0
salary = []
highest_salary = 0



while n < (workers):
    input_salary = int(input("Please enter salary"))
    salary.append(input_salary)
    n += 1
    
highest_salary = max(salary)
print(f"Highest salary is {highest_salary}")
