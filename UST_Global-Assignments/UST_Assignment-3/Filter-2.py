# Write a program using filter() to select all words from a list that start with a vowel.
def fun(s):
    return s[0].lower() in "aeiou"

l=["one","two","three","four"]
print("original list: ",l)
nl=list(filter(fun,l))
print("vowels list: ", nl)