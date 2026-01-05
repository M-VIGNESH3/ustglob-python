import threading
 
def task1():
    for i in range(3):
        print("Thread 1 is running")
 
def task2():
    for i in range(3):
        print("Thread 2 is running")
 
# Create two threads
t1 = threading.Thread(target=task1)   # thread is created  , New 
t2 = threading.Thread(target=task2)
 
# Start the threads
t1.start()                           # runnable , running  , Paused /wait if I/O bounds
t2.start()
 
# Wait for both threads to finish
# t1.join()
# t2.join()
 
print("Main program finished")