import multiprocessing as mp
import time
import os

print os.getpid()

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)
        time.sleep(1)

def dryer(input):
    print("Dryer process started...")
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()
        print('current process pid = ' + str(mp.current_process().pid))

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    print "dryer_proc pid = ", dryer_proc.pid

    dishes = ['salad', 'bread', 'carrots', 'banana']
    washer(dishes, dish_queue)
    dish_queue.join()

