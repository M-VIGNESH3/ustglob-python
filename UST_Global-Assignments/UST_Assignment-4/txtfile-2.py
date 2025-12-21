# Write a program to read the contents of a text file line by line.
f=open("UST_Global-Assignments/UST_Assignment-4/txtfile-2.txt","r")
c=f.readlines()
f.close()
for i in c:
    print(i)