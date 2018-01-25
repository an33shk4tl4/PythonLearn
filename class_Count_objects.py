import os, sys

class someClass(object):
    count = 0

    def __init__(self):
        self.a = "hello"
        self.b = "World!"
        someClass.count +=1

    def setprotectedvar(self,protected_var):
        self._protectedVar = protected_var

    def setprivatevar(self,private_var):
        self.__privateVar = private_var

    def splprint(self,strr):
        """ this object """
        print '*'*10 + str(strr) + '*'*10

    def __del__(self):
        print "I am going to be destroyed!.... {}".format(self.__str__())

c1 = someClass()
c2 = someClass()
c2.setprotectedvar(100)
c2.setprivatevar(999)
print c2._protectedVar
# print c2.__privateVar

print type(someClass) , type(c1)


# c3 = someClass()
# c4 = someClass()
# c5 = someClass()
# c6 = someClass()
print c1.a, c1.b
# print c1.splprint('Hello World!')
print c1.count, c2.count

print dir(c1)
print c1.__dict__

c1._someClass__privateVar = 10

c1.hello =29930040
print "value of hello " , c1.hello

print callable(someClass)
print callable(someClass.count)
print callable(someClass.setprivatevar)
print callable(someClass.setprotectedvar())

