def count_up(n):
    for i in range(1, n + 1):
        yield i
 
for num in count_up(5):
    print(num)