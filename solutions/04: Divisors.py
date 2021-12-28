# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

a = int(input("Please Enter a number: "))
b = [i for i in range(1, a + 1) if a % i == 0]
print(b) 