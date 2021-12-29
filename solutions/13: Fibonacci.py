# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them
# Next Number is the sum of the previous two numbers in the sequence

a = int(input("How many Fibonacci Numbers? (Type '0' to quit): "))
b = []

def fibonacci():

    if a == 0:
        b.clear()
        b.append(0)
        return b
    if a == 1:
        b.clear()
        b.append(1)
        return b
    elif a == 2:
        b.clear()
        b.append(1)
        b.append(1)
        return b

    for i in range(0, 2):
        b.append(1)
    
    b.append(b[0] + b[1])  
    c = 0
    for i in range(1, a - 2):
        c += 1
        b.append(b[c] + b[c + 1])
    return b
    
print(fibonacci())
        