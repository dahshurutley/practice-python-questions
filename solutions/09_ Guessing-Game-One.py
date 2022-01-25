# Generate a random number between 1 and 9 (including 1 and 9)
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random 

a = random.randint(1,9)

while True: 
    b = int(input("Please enter a guess: "))
    if b == a:
        print(f"The Answer was {a}! You Guessed it Correctly.")
        break
    if b < a:
        print("A Little Higher!")
    if b > a:
        print("A Litter Lower!")