from datetime import datetime
import sys

def whiteyear():

    a = datetime.now(tz=None)
    b = a.year

    userName = str(input('Please Enter Your Name: '))
    userAge = int(input('What Is Your Age?: '))

    print(f"{userName}, you will turn 100 in {100 - userAge + b}")

whiteyear()    

        
while True:
    
    a = input("Would you like to go again? 'Y/N'?: ")

    if a == "Y":
        whiteyear()
    else:
        sys.exit()


