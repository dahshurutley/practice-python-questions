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






        


