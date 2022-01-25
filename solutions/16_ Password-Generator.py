import random 
import string

def function(): 
    
    a = []
    for i in range(0, random.randint(1, 3)):
       a.append(random.choice(string.ascii_letters))
       a.append(random.choice(string.digits))
       a.append(random.choice(string.ascii_lowercase))
       a.append(random.choice(string.digits))
       a.append(random.choice(string.punctuation))
    print(f"The Generated Password Is: {''.join(a)}")

function()