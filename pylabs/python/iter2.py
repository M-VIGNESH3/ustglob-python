text = "welcome"
it = iter(text)   # converting str object into an object of iter 
while True:
    try:
        print(next(it))
    except StopIteration:
        break
 
 