# Use map() to add 10 to each element of a given list of numbers.
l=[1,2,3,4,5]
print("Original list",l)
s=map(lambda i:i+10 , l)
print("Squared list",list(s))