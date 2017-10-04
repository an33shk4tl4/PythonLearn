import hline
# hline.h()

# class Person():
#     def __init__(self, name):
#         self.name = name
#         print self.name
#
# # #
# # p1 = Person('hello')
# # print type(p1)
#
# class Male(Person):
#     def __init__(self):
#         pass
#
# p = Person
# m = Male()
#
# p1 = p('hello')
#
#
# print type(Person), type(Male)
# print type(p) , type(m)
# print type(p1)
#
#
# class Car():
#     def exclaim(self):
#         print("I am a car!")
#
# class Yugo(Car):
#     def exclaim(self):
#         print("I am a car too but I am a child car of type Yugo!")
#
#
# c = Car()
# y = Yugo()
#
# c.exclaim()
# y.exclaim()
#
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
#
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"
#
# person = Person('MainClass Person')
#
# md_person = MDPerson('MD Person object')
# print md_person.name
#
# jdperson = JDPerson('aneesh')
# print jdperson.name
#
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         # in any class , the __init__ method supercedes the parent class
#         # __init__ method. so, if needed, it must be explicitly called
#         self.email = email
#
# eperson = EmailPerson('Aneesh','anish@somemail.com')
#
# print type(eperson)


# class Parent(object):
#     def __init__(self):
#         print "hello, I am inside Parent's __init__"
#
#
# class child(Parent):
#     def __init__(self):
#         super(child,self).__init__()
#         print "I am inside child's __init__"
#
#
# p = Parent()
# c = child()


#
# class Duck(object):
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print("inside getter")
#         return self.hidden_name
#     def set_name(self, input_name):
#         print("inside setter")
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
# # name is the attribute , get_name and set_name are methods(properties)
# # of attribute called name
#
# d = Duck('Aneesh')
# print(d.name)
# s = Duck('Srinidhi')
# print(s.name)
#
# # getters and setters using decorators
#
# class PropertyGetterSetter(object):
#     def __init__(self, input_name):
#         self.hidden_input = input_name
#     @property
#     def name(self):
#         # print("inside getter")
#         return self.hidden_input + '_007'
#     @name.setter
#     def name(self, input_name):
#         # print("inside setter")
#         self.hidden_input = input_name
#
#
# c = PropertyGetterSetter('Aneesh Katla')
# print(c.name)
# c.name = 'Katla aneesh'
# print(c.name)
# print('hidden input ' + c.hidden_input)
# c.hidden_input = 'Whatevernamehahah'
# print('hidden input ' + c.hidden_input)
# print(c.name)
#
# hline.h()

class NewClass(object):
    def __init__(self, input_name):
        self.__hidden_input = input_name
    _someprop = 10
    @property
    def name(self):
        return self.__hidden_input
    @name.setter
    def name(self, input_name):
        self.__hidden_input = input_name

newclass = NewClass('NewClass')
print('getter = ' + newclass.name)
print('calling setter')
newclass.name = 'nidhi'
print('getter = ' + newclass.name)
print(newclass._someprop)
hline.h()
# newclass._someprop = 12
# hline.h()
# print(newclass._someprop)
# print(newclass.__hidden_input)
hline.h()
print(newclass._NewClass__hidden_input)
# newclass._NewClass__hidden_input = 'aneeshkatla'
print(newclass._NewClass__hidden_input)
print(newclass.name)
print('done')
print(newclass.__dict__)
