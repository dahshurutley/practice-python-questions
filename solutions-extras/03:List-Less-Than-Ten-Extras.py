a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

print("Finding integers less than the given number within a list: ")

def lessthan():
    print('Numbers Less than 5: ')
    for i in a: 
        if i < 5:
            b.append(i)
    
    print(b)
    print('')
    manager()


def userIn():
    
    numIn = int(input("Please Input a Number: "))
    print(f'Numbers Less than {numIn}: ')
    c = []
    for i in a:
        if i < numIn:
            c.append(i)

    print(c)
    print('')
    manager()
            

def manager(): 

    userInput = str(input("'M' to enter user version \n'N' To Enter normal version\n'Enter' to exit: ")).capitalize()

    if userInput == 'M':
        userIn()
    
    if userInput == 'N':
        lessthan()

manager()






        


