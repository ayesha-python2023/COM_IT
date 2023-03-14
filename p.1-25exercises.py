## Calculate the salary increase for a group of employees of a company considering the following criteria: 
## If the salary is less than $ 1,000.00: Increase 15%. If the salary is greater than or equal to $ 1,000.00: 
## Increase 12%. The program must do The following: 
## Save the new salaries in the arrangement - Calculate the payroll - Print the salaries from the settlement


salary_per_individual = int(input("Please enter your salary: "))

#######if we assume the tax is going to be 10%
if salary_per_individual < 1000 and salary_per_individual > 0:
    new_salary = salary_per_individual * 0.15
    print(f"Your new salary is {new_salary}")
   
elif salary_per_individual >= 1000:
    new_salary = salary_per_individual * 0.12
    print(f"Your new salary is {new_salary}")

else:
    print("Please enter a valid amount")

tax = new_salary * 0.10
print(f"Your new income after tax will be {new_salary - tax}")
