# Write a program using map() to convert all strings in a list to uppercase
l=["one","two","three"]
print("Original list: ",l)
nl= map(lambda i:i.upper(),l)
print( "Modified list: ",list(nl))