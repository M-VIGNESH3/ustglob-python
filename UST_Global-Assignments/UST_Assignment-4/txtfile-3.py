# Write a Python program to count the number of lines,
#  words, and characters in a text file.
f=open("UST_Global-Assignments/UST_Assignment-4/txtfile-3.txt","r")
con=f.readlines()
f.close()
n=len(con)
w=0
ch=0

for i in con:
    w+=len(i.split(" "))
    ch+=sum([len(j) for j in i.split(" ")])
    # ch+=len(i)

print("number of lines : ",n)
print("number of words : ", w)
print("number of characters :",ch)