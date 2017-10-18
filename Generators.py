# create a generator function to generate 1000 even numbers

def gen_Even_numbers(first=0, last=1000, step=1):
    n = first
    while n < last:
        if n%2 == 0:
            yield n
        n += step

print 'Type of gen_Even_numbers = ', type(gen_Even_numbers)

# set a new variable object generator
ge = gen_Even_numbers(first=1,last=999)

print 'Type of ge = ', type(ge)

for i in ge:
    print i

#TODO
# n = yield n --> check this out on Jeff Knupp's blog its about
# sending values to generator function, yet to learn this concept


print """
*****proper understanding of generators
A generator is a function which returns a iterable
any function with yield keyword is a generator
Generator input arguments optional
variable = some_generator_function() returns iterable object that
            can be consumed using next(variable)
For example:
a = gen_list_nums()

print next(a) , next(a),next(a) , next(a),next(a) , next(a)
print a.next(), a.next(), a.next(), a.next()

"""

def gen_list_nums():
    n = 0
    while n < 100:
        yield n
        n += 1

a = gen_list_nums()

print next(a) , next(a),next(a) , next(a),next(a) , next(a)
print a.next(), a.next(), a.next(), a.next()

