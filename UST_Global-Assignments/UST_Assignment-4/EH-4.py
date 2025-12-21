# Write a Python program that uses try, except, else, and finally blocks.

n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
try: 
    print(n1/n2)
except ZeroDivisionError as z:
    print(z)
    print("dividing with 0 is invalid")
else:
    print("this is in else block")
finally:
    print("this is in finally block")
    print("program executed completely10")