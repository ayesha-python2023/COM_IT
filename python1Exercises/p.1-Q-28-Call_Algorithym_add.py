# Write an algorithm that calls another name "add", which receives 2 numbers. 
#The summation algorithm must add its parameters. 
#The algorithm you invoke must receive that value and display it on the screen.

import add_my_numbers


number_1 = int(input("Enter a two digit number: "))
number_2 = int(input("Enter a two digit number: "))
    

numbers_sum = add_my_numbers.add(number_1, number_2)
print(numbers_sum)