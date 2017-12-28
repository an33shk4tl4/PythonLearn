# simple multithreading example with a variable
# number of worker threads
from Queue import Queue
from threading import Thread
import threading
import time

q = Queue()
num_worker_threads = 20
def do_work(item):
    print("****doing work on {0} ".format(item))
    print("using thread {0} ".format(threading.currentThread()))
    time.sleep(1)

def worker():
    while True:
        item = q.get()
        print("got item {0} ".format(str(item)))
        do_work(item)
        q.task_done()

for i in range(num_worker_threads):
     t = Thread(target=worker,args=())
     t.daemon = True
     t.start()
print "Threads initiated.."

print "putting items to queue.."

for i in range(20):
    q.put(i)
    print "Item {0} has been added".format(str(i))
    # time.sleep(2)

q.join()       # block until all tasks are done
