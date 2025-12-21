# Given a list of integers, use filter() to remove all negative numbers.

l=[-1,-2,-3,-4,1,2,3,4]
print("original list: ",l)
p=filter(lambda i:i>=0 ,l)
print("positive numbers list: ",list(p))