# Write a Python program using filter() to extract all even numbers from a list.
l=[1,2,3,4]
print("original list: ",l)
e=filter(lambda i:i%2==0 ,l)
print("even numbers list: ",list(e))