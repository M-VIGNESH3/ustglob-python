def outer():
    x = 10
    def inner():
        x=x+1     # we can access variable declared outside but can not be
        print(x)  # modified  
 
    inner()
    print(x)
 
outer()  