# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

a = int(input('Please Enter a number: '))

if a % 2 == 0: 
    print('The Number is Even!')
else:
    print('The Number is Odd!')

# Extra 1 in this solution
if a % 4 == 0:
    print('The number is a multiple of 4! (and therefore even)')
