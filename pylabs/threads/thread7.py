import threading
 
def print_message(name, count):
    for i in range(count):
        print(f"Hello {name}")
 
# Create two threads with arguments
t1 = threading.Thread(target=print_message, args=("Alice", 10))
t2 = threading.Thread(target=print_message, args=("Bob", 10))
 
# Start the threads
t1.start()
t2.start()
 
# Wait for both threads to finish
t1.join()
t2.join()
 
print("Main program finished")