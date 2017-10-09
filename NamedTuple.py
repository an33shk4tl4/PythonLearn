from collections import namedtuple


d = namedtuple('Address','street city zipcode')

a1 = d('Street Address Whatever', 'Fayetteville', '72703')

print(a1)
print a1.street, a1.city , a1.zipcode
a2 = a1
print(a2)
a3 = a2._replace(city='Bentonville')
a2 = None
print a1, a2, a3
