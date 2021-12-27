num = int(input('Please Enter a number: '))
check = int(input(f'Please input number you want {num} to be divided by: '))

if num % check != 0: 
    print(f"{check} does not divide evenly into {num}!")

elif num % check == 0:
    print(f"{check} does divide evenly into {num}!")

