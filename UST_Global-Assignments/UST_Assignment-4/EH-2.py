# Write a program that accepts user input and 
# handles a ValueError if the input is not an integer.

a=input("enter any number: ")
try :
    a=int(a)
    print("your number is : ",a)
except ValueError as e:
    print(e)
    print("Invaid !,",a, "is not a number")