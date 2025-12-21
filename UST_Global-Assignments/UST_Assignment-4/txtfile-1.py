# Write a Python program to create a text file and write multiple lines into it.
f=open("UST_Global-Assignments\UST_Assignment-4\txtfile-1.txt","w")
n=int(input("enter number of key and value pairs:"))
f.write("key:value \n")
for i in range(n):
    name=input("Enter key: ")
    marks=input("Enter value: ")
    f.write(name+":"+(marks)+"\n")

f.close()