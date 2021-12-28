#Ask the user for a string and print out whether this string is a palindrome or not. 
import string 

a = str(input('Please Enter String: ')).upper()
b = [i for i in a]

if b == b[::-1]:
    print("This String is a Palindrome")
else:
    print("This String is not a Palindrome")




