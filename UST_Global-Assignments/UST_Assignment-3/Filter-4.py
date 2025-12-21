# Write a program using filter() to find numbers greater than 50 from a list.

l=[20,30,40,50,60,70,80]
print("original list: ",l)
nl=filter(lambda i:i>50 ,l)
print("greater than 50 numbers in list: ",list(nl))