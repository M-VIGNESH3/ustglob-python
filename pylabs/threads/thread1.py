import threading
import time

c=0
def fun():
    global c
    for _ in range(100000):
        temp = c          # read
        time.sleep(0)     # force context switch
        c = temp + 1   

t=[]
for i in range(4):
    x=threading.Thread(target=fun)
    t.append(x)

for i in t:
    i.start()
    

for i in t:
    i.join()

print(c)