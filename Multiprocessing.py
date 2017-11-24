import multiprocessing
import os
import datetime

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process {} says : {}".format(os.getpid(), what))

if __name__ == '__main__':
    whoami("I am the main program")
    for n in range(4):
        # p = multiprocessing.Process(target=do_this, args=("I am function {0}".format(str(n)),))
        p = multiprocessing.Process(target=do_this, args=("I am function {0}".format(str(datetime.datetime.now())),))
        p.start()

