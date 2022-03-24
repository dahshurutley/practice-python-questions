# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.


import random
# Cow = Correct Placement 
# Bull = Wrong Place Correct Guess
NUM = random.randint(1000, 10000)
SOLUTION = [i for i in str(NUM)]
print(''.join(SOLUTION))

cow = 0
bull = 0 
counter = 0 

# clear user input upon each guess

while True: 
  user_input = str(input('Guess a 4 digit number'))
  guess  = [i for i in user_input]
  counter += 1
  
  for i in guess: 
    if guess.index(i) in SOLUTION:
      if guess.index(i) == SOLUTION.index(i):
        cow += 1
      else: 
        bull += 1
    if user_input == ''.join(SOLUTION):
      print(f'You Have {cow} cows!')
      print(f'You have {bull} bulls!')
      break 
      
        
        