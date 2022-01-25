# No Extras
# Personal Extra: Restart until said otherwise

import random 
import string
import sys

def restart():

    a = input("Do you want to generate another password Y/N?: ").upper()
    if a == "Y":
        function() 
    if a == "N":
        print("Closing\n")
        sys.exit()

def function(): 
    
    a = []
    for i in range(0, 2):
       a.append(random.choice(string.ascii_letters))
       a.append(random.choice(string.digits))
       a.append(random.choice(string.ascii_lowercase))
       a.append(random.choice(string.digits))
       a.append(random.choice(string.punctuation))
    print(f"The Generated Password Is: {''.join(a)}\n")
    restart()

function()





