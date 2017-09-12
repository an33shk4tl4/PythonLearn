import os
def documentit(func):
    def new_function(*args,**kwargs):
        print('Running function',func.__name__)
        print('Positional arguments', args)
        print('Keyword arguments', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
    return new_function

def deco2(func):
    def multiply1000(a,b):
        print a , b
        print func.__name__
        return func(a,b)*1000
    return multiply1000

def hline(str,lnth):
    return '#'*lnth + ' ' + str + ' ' + '#'*lnth


def deco3(func):
    def multiply1000(*args):
        print(args)
        print hline(func.__name__, 40)
        return func(*args)*1000
    return multiply1000

# @documentit

@deco3
def aintsss(a, b):
    return a * b

print(aintsss(3, 4))
print('*'*10)
c2 = deco2(aintsss)
c2(3, 4)
