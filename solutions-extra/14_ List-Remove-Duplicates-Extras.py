# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
import random

a = [random.randrange(2, random.randint(6, 23), 2) for i in range(random.randint(2,10))]
b = [random.randrange(2, random.randint(6, 23), 2) for i in range(random.randint(2,10))]

def function():
    c = {i for i in b if i in a}
    return c

while len(function()) == 0:
    print(f"First List: {a}")
    print(f"Second List: {b}")
    print("There are no shared Elements!")
    break

while len(function()) > 0:
    print(f"First List: {a}")
    print(f"Second List: {b}")
    print(f"Shared Elements: {function()}")
    break



