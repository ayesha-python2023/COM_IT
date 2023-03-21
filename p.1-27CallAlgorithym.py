#lets suppose we are trying to make an algorithym to find out the table of N number:

def table_of_N_number(numberN: int, result: int) -> int:
    result = 0
    i = 0
    while i < 11:
        calculation = i * numberN
        result = calculation
        print(f"{numberN} * {i} = {result}")
        i += 1
        

    return(result)
#Now we can take any input from the user and get the table of that number:
number_string = input("Please enter a number to get its table")
number = int(number_string)

table_of_10 = table_of_N_number(number, 10)

print(table_of_10)