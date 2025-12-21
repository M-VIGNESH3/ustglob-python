# Use filter() to extract all palindromic strings from a list.

def pan(s):
    s=s.lower()
    return s==s[::-1]

l=["one","two","eye","three","Mom"]
print("original list: ",l)
nl=list(filter( pan,l))
print("all palindromic strings in the list: ",list(nl))