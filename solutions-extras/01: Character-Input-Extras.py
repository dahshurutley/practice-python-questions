# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# Print out that many copies of the previous message on separate lines.
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


