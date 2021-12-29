# No Extras
# Repeated Input
import sys

def function():

    a = str(input('Please Enter a Random Sentance, or Random words\n("exit" [Case Sensative] to Quit): \n\n'))
    if a == 'exit':
        sys.exit()
    b = a.split()
    b.reverse()
    c = ' '.join(b)
    print(f"{c}\n")
    function()
    
function()







