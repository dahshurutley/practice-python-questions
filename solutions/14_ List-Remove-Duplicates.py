# Return a new list that contains all the elements of the first list minus all the duplicates.
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Using a list for this question is inefficent. 
import random

a = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
print(f"Original List: {a}")
print(f'List Without Duplicates: { {i for i in a} }')


        


        








