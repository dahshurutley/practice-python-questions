# Take a list and write a program that prints out all the elements of the list that are less than 5.
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list...
# ...That are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Finding integers less than the given number within a list: ")
def lessthan():
    print('Numbers Less than 5: ')
    print([i for i in a if i < 5])
    print('')
    manager()

def userIn():
    
    numIn = int(input("Please Input a Number: "))
    print(f'Numbers Less than {numIn}: ')
    print([i for i in a if i < numIn])
    print('')
    manager()
            
def manager(): 

    userInput = str(input("'M' to enter user version \n'N' To Enter normal version\n'Enter' to exit: ")).capitalize()
    if userInput == 'M':
        userIn()
    if userInput == 'N':
        lessthan()

manager()






        


