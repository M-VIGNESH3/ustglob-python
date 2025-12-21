# Write a program to copy the contents of one text file into another file.
f1=open("UST_Global-Assignments/UST_Assignment-4/txtfile-3.txt","r")
con=f1.read()
f1.close()
f2=open("UST_Global-Assignments/UST_Assignment-4/txtfile-4.txt","w")
f2.write("content is copied  form another file \n")
f2.write(con)
f2.close()