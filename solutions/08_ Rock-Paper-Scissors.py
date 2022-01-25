# Make a two-player Rock-Paper-Scissors game.
# Using Automated Responses for Player 2 (Computer)
import random
choices = ['SCISSORS', 'PAPER', 'ROCK']
a = random.choice(choices)
print("Welcome to Rock, Paper, Scissors!")
print(f"Possible Choices: {choices}")

def manager():
    a = str(input("Do you want to go again? Y/N: ")).upper()
    if a == "Y":
        rps()

def rps():

    player1 = str(input('Please Choose from the Three operators: ')).upper()
    
    if player1 == 'ROCK':
        
        if a == 'SCISSORS':
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, The Computer Wins!\nRestarting Program...")
            manager()
        if a == player1:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, It's A Tie!\nRestarting Program...")
            manager()

    if player1 == 'SCISSORS':
        if a == "PAPER":
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, The Computer Wins!\nRestarting Program...")
            manager()
        if a == player1:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, It's A Tie!\nRestarting Program...")
            manager()

    if player1 == 'PAPER':
        if a == 'ROCK':
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, The Computer Wins!\nRestarting Program...")
            manager()
        if a == player1:
            print(f"Player One Chose {player1},\nThe Computer Chose {a}, It's A Tie!\nRestarting Program...")
            manager()

    if player1 not in choices:
            print("Please Enter one of the Three Choices!\n")

rps()

    