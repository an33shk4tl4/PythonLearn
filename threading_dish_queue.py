import threading, Queue
import time
import os

print os.getpid()
dish_queue = Queue.Queue()

def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing ", dish)
        dish_queue.put(dish, True, 4)
        time.sleep(1)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get(True, 2)
        # time.sleep(2)
        print("Drying {}".format(threading.current_thread()), dish)
        dish_queue.task_done()
        # print("Dish queue empty ? = {}".format(dish_queue.empty()))

print(threading.current_thread())

if __name__ == '__main__':
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.setDaemon(True)
        dryer_thread.start()
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()
