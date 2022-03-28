# Create a program that will play the “cows and bulls” game with the user. 

# The game works like this:
  # Randomly generate a 4-digit number. 
  # Ask the user to guess a 4-digit number. 
  # For every digit that the user guessed correctly in the correct place, they have a “cow”. 
  # For every digit the user guessed correctly in the wrong place is a “bull.” # 
  # Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
  # Once the user guesses the correct number, the game is over. 
  # Keep track of the number of guesses the user makes throughout the game and tell the user at the end.


import random
NUM = random.randint(1000, 10000)
SOLUTION = [i for i in str(NUM)]

cow = 0
bull = 0 
counter = 0 


while True: 
  user_input = str(input('Guess a 4 digit number: '))
  guess  = [i for i in user_input]
  print(guess)
  counter += 1
  
  # If user_input == SOLUTION, end game and print amount of guesses. 
  if user_input == ''.join(SOLUTION):
      print(f'Correct, the number was {"".join(SOLUTION)}, it took you {counter} tries!')
      break 
  if len(user_input) != 4: 
      print('Not a 4 digit number')
      break

  # Evaluator
  for i in range(0, len(SOLUTION)): 
      if guess[i] in SOLUTION:
        if guess[i] == SOLUTION[i]:
          cow += 1
        if guess[i] != SOLUTION[i]:
          bull += 1 
        
  print(f'You have {cow} cows and {bull} bulls.')

  # Clears values for next user input
  bull = bull - bull
  cow = cow - cow
    
  
         
        