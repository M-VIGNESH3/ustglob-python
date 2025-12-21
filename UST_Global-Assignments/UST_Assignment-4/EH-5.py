# Write a program to handle multiple exceptions in a single try block.


try: 
    n1=int(input("enter 1st number: "))
    n2=int(input("enter 2nd number: "))
    print(n1/n2)
except ZeroDivisionError as z:
    print(z)
    print("dividing with 0 is invalid")
except ValueError as v:
    print(v)
    print("one of your inputs is not a number")