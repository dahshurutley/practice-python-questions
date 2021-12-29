# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.

def function():

    a = str(input('Please Enter a Random Sentance, or Random words: '))
    b = a.split()
    b.reverse()
    c = ' '.join(b)
    return c

print(function())

