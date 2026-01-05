def outer():
    x = 10
    def inner():
        print(x)
        
    inner()
    print(x)
 
outer()