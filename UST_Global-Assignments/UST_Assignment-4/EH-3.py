# Write a program to open a file and handle a FileNotFoundError.

try: 
    f=open("filennotfound.txt","r")
    c=f.read()
    print(c)
except FileNotFoundError as e:
    print(e)
    

