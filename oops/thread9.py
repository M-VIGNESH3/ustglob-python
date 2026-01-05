import threading
 
count = 0
lock = threading.Lock()
 
def increment():
    global count
    for _ in range(100000):
        lock.acquire()      # lock the resource
        count += 1
        lock.release()      # release the resource
 
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
 
t1.start()
t2.start()
 
t1.join()
t2.join()
 
print("Final count:", count)