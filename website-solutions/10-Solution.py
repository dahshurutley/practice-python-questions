# Write a program that returns a list that contains only the elements that are common between the lists 
# No Duplicates
# Solution already in 05: List Overlap 

import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]
