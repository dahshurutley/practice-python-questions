# Write a program that takes a list of numbers 
# Make a new list of only the first and last elements of the given list.
# No Extras 
# Personal Extra: Generate List with Random Values

import random

a = [random.randrange(1, random.randint(3, 25), 3) for i in range(random.randint(3,10))]
print(f"Generated List: {a}")
print(f"Beginning and End Points: {list(a[0:len(a):len(a) - 1])}") 