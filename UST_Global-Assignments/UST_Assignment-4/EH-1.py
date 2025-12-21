# Write a Python program to handle a ZeroDivisionError.
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
try: 
    print(n1/n2)
except ZeroDivisionError as z:
    print(z)
    print("dividing with 0 is invalid")