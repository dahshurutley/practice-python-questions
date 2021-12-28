# Take two lists and write a program that returns a list that contains elements that are common between the lists
# Make sure your program works on two lists of different sizes
# Randomly generate two lists to test this
# Write this in one line of Python

import random

a = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
b = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
c = [i for i in b if i in a]

print(f"First List: {a}")
print(f"Second List: {b}")
print(f"Shared Elements: {c}")

