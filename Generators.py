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

