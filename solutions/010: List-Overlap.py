# Write a program that returns a list that contains only the elements that are common between the lists 
# No Duplicates
# Solution already in 05: List Overlap


import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [i for i in b if i in a]

print(f"First List: {a}")
print(f"Second List: {b}")
print(f"Shared Elements: {c}")