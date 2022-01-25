# Write a program that returns a list that contains only the elements that are common between the lists 
# No Duplicates
# Extra: Generate Lists Manualy
# Solution already in 05: List Overlap

import random

a = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
b = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
c = [i for i in b if i in a]

print(f"First List: {a}")
print(f"Second List: {b}")
print(f"Shared Elements: {c}")