class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I am in A")
    @classmethod
    def call_class_mthd(cls):
        print("A has {} little objects".format(cls.count))

    @staticmethod
    def call_staticmethod():
        print "hello, this is a static method call"
        print "Static method can access class variable , A.count = ", A.count
        A.count = 100
        print "Static method can access class variable , A.count = ", A.count

easy_a = A()
breezy_a = A()
wheezy_a = A()
wheezy_b = A()

A.call_class_mthd()
A.call_staticmethod()
wheezy_b = A()

A.call_class_mthd()
A.call_staticmethod()
