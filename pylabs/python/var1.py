def outer():
    x = 10
    def inner():
        x = 20   # This creates a NEW local variable
        print(x)
 
    inner()
    print(x)
 
outer()   # 10,1,2,7,3,4,5,8