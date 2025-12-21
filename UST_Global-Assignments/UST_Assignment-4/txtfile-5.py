# Write a Python program to search for a specific word in a text file 
# and display the line numbers where it appears.

w = input("Enter the word to search: ")

f = open("UST_Global-Assignments/UST_Assignment-4/txtfile-5.txt", "r")

ln = 1
found = False

for line in f:
    if w in line:
        print("Word found at line:",ln)
        found = True
    ln += 1

f.close()

if not found:
    print("Word not found in the file.")