### Write a program that asks for a numerical password and allows three attempts. 
#If the user enters the correct password, it shows "Correct!" And run any program, after the message.
#Otherwise the program should display "Wrong password". Then finish the program immediately.

numerical_password = 0
password_attempt = 0
correct_password = 123456789

while password_attempt < 3:
    numerical_password = input("Please enter a password that only contains numbers: " )
    entered_password = print(numerical_password)
    if numerical_password == correct_password:
        print("You got it right.")
    else:
        print("Password you entered is not correct.")
    password_attempt += 1
