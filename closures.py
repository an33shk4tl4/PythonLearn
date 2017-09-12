"""
closure is a dynamically created function
that remembers where it came from
"""
import datetime as dt
import time

def knights2(saying):
    def inner2():
        return str(dt.datetime.today()) + ' ' + saying
    return inner2

a = knights2('Hello')

type(a)
print a()

time.sleep(60)
b = knights2('Aneesh')

type(b)
print b()

time.sleep(60)
print a()
print b()





