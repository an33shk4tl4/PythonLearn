#Lists tutorial

__author__ = 'akatla'

#everything about lists

a=['Sunday','Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']

# print a[0]

weeks_tuples=('Sunday','Monday', 'Tuesday', 'Wednesday','Thursday','Friday',\
       'Saturday')

# print weeks_tuples[1]
print weeks_tuples[2:3]

weeks_list = ['Sunday','Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']
print 'print weeks_list'
print weeks_list

weeks_list.append('newday')
print weeks_list

del weeks_list

# Map 2 lists into a dict

keys = ['Sunday','Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']
values = [1,2,3,4,5,6,7]
# newdict = dict(zip(keys,values))
week_dict = dict(zip(keys,values))
print week_dict

#delete/remove a list item by value 
del list[index]

#to get index of an item in a list
list.index('<value>') 
# watch out for duplicate values and the index , 
#it behaves weird when index is called on a value that has duplicates in the list

list.remove  #another method to remove a list item by value

