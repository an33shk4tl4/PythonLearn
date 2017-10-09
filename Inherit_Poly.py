import datetime
import time
import logging
import os , sys



# class ParentClass(object):
#     def __init__(self):
#         self.word = 'Hello'
#
# class ChildClass(ParentClass):
#     """ note the usage of init method inside child class
#     its different but works only for new-style parent - child class
#     declaration"""
#     def __init__(self):
#         super( ChildClass,self).__init__()
#
# a = ParentClass()
# print "a.word in parentclass = ", a.word
#
# b = ChildClass()
# print "word in child class = ", b.word

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

root.info('This is a info message')
root.debug('This is a DEBUG level message')
root.critical('This is a CRITICAL message')
root.fatal('This is a FATAL  message, but displays CRITICAL perhaps both are same!!')

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

class Book():
    def __init__(self):
        self.create = datetime.datetime.now()


b = Book()

print(b.create)

# time.sleep(5)

print(b.create)

# duck typing

# if a function can call method on any object as long as
# the right/valid method is called, its allowed in compile time
# meaning it throws error only during runtime

class Sparrow:
    def fly(self):
        print("Sparrow flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

sparrow = Sparrow()
airplane = Airplane()
whale = Whale()
try:
    lift_off(sparrow) # prints `Sparrow flying`
    lift_off(airplane) # prints `Airplane flying`
    lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
except Exception as e:
    print e.message

