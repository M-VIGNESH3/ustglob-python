import threading
 
def task():
    print("This is a thread")
 
t = threading.Thread(target=task)
t.start()  
t.join()