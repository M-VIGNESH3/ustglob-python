# Write a program using map() to calculate the length of each word in a list of strings.
l=["one","two","three","four"]
rl=map(lambda i:len(i) , l)
print(list(rl))