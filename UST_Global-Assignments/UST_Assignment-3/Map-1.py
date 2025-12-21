# Write a Python program using map() to convert a list of integers into their squares

l=[1,2,3,4,5]
print("Original list",l)
s=map(lambda i:i**2 , l)
print("Squared list",list(s))