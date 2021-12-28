# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input('Please Enter a number: '))
check = int(input(f'Please input number you want {num} to be divided by: '))

if num % check != 0: 
    print(f"{check} does not divide evenly into {num}!")

elif num % check == 0:
    print(f"{check} does divide evenly into {num}!")

