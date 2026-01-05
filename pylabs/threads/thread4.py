import threading
import time
 
def task():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")
 
t = threading.Thread(target=task)
print("Thread created")      # New
t.start()                    # Runnable → Running
# t.join()                     # Terminated
print("Main program ends")