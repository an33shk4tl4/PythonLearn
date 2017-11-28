import threading
import os

print os.getpid()

i = 0

def do_this(what):
    global i
    whoami(what)
    i += 1
    print i,


def whoami(what):
    print("Thread {0} says : {1}".format(threading.current_thread(), what))

if __name__ == '__main__':
    whoami("I am in the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I am function {}".format(str(n)),))
        p.start()

