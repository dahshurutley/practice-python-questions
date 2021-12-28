# Creating a Extra!: Generate Random List
import random 
a = [random.randrange(1, random.randint(6, 23), 1) for i in range(random.randint(1,10))]
print([i for i in a if i % 2 == 0])
