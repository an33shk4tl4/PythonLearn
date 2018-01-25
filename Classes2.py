class NewClass(object):
    count = 100
    def __init__(self, input_name):
        self.hidden_name = input_name
        self.__name = 'hidden value'

    @classmethod
    def SomeClassMethod(cls):
        print("inside class method - calling..")
        print ("showing value of cls.count = {}".format(cls.count))

    @classmethod
    def SomeClassMethod1(cls,self):
        print("inside class method - calling..")
        print ("showing value of cls.count = {}".format(cls.count))
        print "value of object.name = {}".format(self.name)

    @staticmethod
    def SomeStaticMethod():
        print("Inside Static method")
        print ("showing value of cls.count = {}".format(NewClass.count))

    @staticmethod
    def SomeStaticMethod1(self):
        print("Inside Static method")
        print ("showing value of cls.count = {}".format(NewClass.count))
        print "value of object.name = {}".format(self.name)

    @property
    def name(self):
        print("inside getter")
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.hidden_name = input_name
    @property
    def get_private_name(self):
        return self.__name
    @get_private_name.setter
    def get_private_name(self,input_name):
        self.__name = 'new hid value'
# class method and static methods can be called without instantiation

# object reference can be passed to class or static methods
# and relevant object methods can be called.

NewClass.SomeClassMethod()
NewClass.SomeStaticMethod()

a = NewClass("Aneesh")
print a.name
NewClass.SomeClassMethod1(a)
print 100*"*"
NewClass.SomeStaticMethod1(a)

a.name = 'Katla'
print a.name
print a.get_private_name
a.get_private_name = 'whatever'
print a.get_private_name
