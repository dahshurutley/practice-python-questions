# Generate a random number between 1 and 9 (including 1 and 9)
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random 
import sys

a = random.randint(1,9)

def manager():

    a = input("Do you want to play again? Y/Exit?: \n").lower()
    if a == 'exit':
        sys.exit()
    if a == 'y':
        guessing()
        
def guessing():

    c = 0
    while True: 
        c += 1
        b = int(input("Please enter a guess: "))
        if b == a:
            print(f"The Answer was {a}! You Guessed it Correctly.")
            print(f"You guessed it in {c} Tries!")
            manager()
        if b < a:
            print("A Little Higher!")
        if b > a:
            print("A Litter Lower!")
        
    

guessing()
