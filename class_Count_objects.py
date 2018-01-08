import os, sys

class someClass(object):
    count = 0
    def __init__(self):
        self.a = "hello"
        self.b = "World!"
        someClass.count +=1

    def splprint(self,strr):
        """ this object """
        print '*'*10 + str(strr) + '*'*10

c1 = someClass()
c2 = someClass()
c3 = someClass()
c4 = someClass()
c5 = someClass()
c6 = someClass()
print c1.a, c1.b
print c1.splprint('Hello World!')
print c1.count, c2.count, c3.count
