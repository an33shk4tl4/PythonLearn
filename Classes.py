class Person():
    def __init__(self, name):
        self.name = name
        print self.name

# #
# p1 = Person('hello')
# print type(p1)

class Male(Person):
    def __init__(self):
        pass

p = Person
m = Male()

p1 = p('hello')


print type(Person), type(Male)
print type(p) , type(m)
print type(p1)


class Car():
    def exclaim(self):
        print("I am a car!")

class Yugo(Car):
    def exclaim(self):
        print("I am a car too but I am a child car of type Yugo!")


c = Car()
y = Yugo()

c.exclaim()
y.exclaim()

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('MainClass Person')

md_person = MDPerson('MD Person object')
print md_person.name

jdperson = JDPerson('aneesh')
print jdperson.name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        # in any class , the __init__ method supercedes the parent class
        # __init__ method. so, if needed, it must be explicitly called
        self.email = email

eperson = EmailPerson('Aneesh','anish@somemail.com')

print type(eperson)


