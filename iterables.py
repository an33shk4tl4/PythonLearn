# iterating over multiple lists using zip
import pprint as pp
import os

days = ['Monday', 'tuesday', 'wednesday']
fruits = ['banana', 'orange', 'peach']

desserts = zip(days, fruits)

pp.pprint(desserts)

# raw_input('Please hit a key to proceed further')

os.system('pause')
print('End of program')

