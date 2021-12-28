# Make a two-player Rock-Paper-Scissors game.
import random
choices = ['SCISSORS', 'PAPER', 'ROCK']
print("Welcome to Rock, Paper, Scissors!")
print(f"Possible Choices: {choices}")

player1 = str(input('Please Choose from the Three operators: ')).upper()
player2 = str(input('Please Choose from the Three operators: ')).upper()

if player1 not in choices:
    print("Unregistered Responses... Restart Program.")
elif player2 not in choices:
    print("Unregistered Responses... Restart Program.")


def manager():
    a = str(input("Do you want to go again? Y/N: ")).upper()
    if a == "Y":
        rps()

def rps():

    if player1 == 'ROCK':
        
        if player2 == 'SCISSORS':
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player Two Wins!\nRestarting Program...")
            manager()
        if player2 == player1:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, It's A Tie!\nRestarting Program...")
            manager()

    if player1 == 'SCISSORS':
        if player2 == "PAPER":
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player Two Wins!\nRestarting Program...")
            manager()
        if player2 == player1:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, It's A Tie!\nRestarting Program...")
            manager()

    if player1 == 'PAPER':
        if player2 == 'ROCK':
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player One Wins!\nRestarting Program...")
            manager()
        else:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, Player Two Wins!\nRestarting Program...")
            manager()
        if player2 == player1:
            print(f"Player One Chose {player1}, Player Two Chose {player2}, It's A Tie!\nRestarting Program...")
            manager()


rps()

    