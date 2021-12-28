# Ask the user for a number and determine whether the number is prime or not.

def prime():

    a = int(input('Please Enter Number:  '))
    b = [i for i in range(1, a + 1) if a % i == 0]
    
    if len(b) > 2:
        print(f"Factors: {b}")
        print(f"The Number {a} is not prime!")
    if len(b) == 2:
        print(f"Factors: {b}")
        print(f"The Number Is Prime!")
    if a == 1: 
        print(f"{a} is never prime!")
    if a == 0:
        print(f"{a} is never prime!")


prime()



