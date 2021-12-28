# No Extras
# Creating own Extra that detects repeated Input from user


def prime():

    a = int(input('Please Enter Number (Enter "1" to Quit!):  '))
    b = [i for i in range(1, a + 1) if a % i == 0]

    if len(b) > 2:
        print(f"Factors: {b}")
        print(f"The Number {a} is not prime!\n")
        prime()
    if len(b) == 2:
        print(f"Factors: {b}")
        print(f"The Number Is Prime!\n")
        prime()
    if a == 1: 
        print(f"{a} is never prime!....Closing Program\n")
    if a == 0:
        print(f"{a} is never prime!\n")
        prime()

prime()




