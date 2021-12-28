# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime

def whiteyear():

    a = datetime.now(tz=None)
    b = a.year

    userName = str(input('Please Enter Your Name: '))
    userAge = int(input('What Is Your Age?: '))

    print(f"{userName}, you will turn 100 in {100 - userAge + b}")

whiteyear()




    
