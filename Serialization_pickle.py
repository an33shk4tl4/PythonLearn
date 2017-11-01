import pickle
import datetime
import time
import hline as h


now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
h.h()
time.sleep(10)
now2 = pickle.loads(pickled)
print pickled
print datetime.datetime.utcnow(), now2, now1
h.h()

class Tiny(object):
    def __str__(self):
        return 'TINY'

obj1 = Tiny()
print str(obj1) , type(obj1)

pickled = pickle.dumps(obj1)
print 'pickled = ', str(pickled), type(pickled)
h.h()
obj2 = pickle.loads(pickled)

print 'un-pickled = ', str(obj2), type(obj2)
h.h()
