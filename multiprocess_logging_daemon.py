import multiprocessing
import os
import datetime
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(processName)-10s) (%(threadName)-10s) %(message)s', )


def do_this(what):
    whoami(what)
    # print("before sleep pid = {}".format(os.getpid()))
    logging.debug('before sleep')
    print(int(os.getpid()%10.0))
    time.sleep(int(os.getpid()%10.0))
    logging.debug('after sleep')
    # print("after sleep pid = {}".format(os.getpid()))

def whoami(what):
    logging.debug('running whoami function for {}'.format(what))
    # print("Process {} says : {}".format(os.getpid(), what))


if __name__ == '__main__':
    whoami("I am the main program")
    for n in range(4):
        # p = multiprocessing.Process(target=do_this, args=("I am function {0}".format(str(n)),))
        p = multiprocessing.Process(target=do_this, args=("I am function {0}".format(str(datetime.datetime.now())),))
        p.start()
        # p.join()
    print("***********outside for loop..")
