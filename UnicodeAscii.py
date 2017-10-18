'''unicode contains currently defined character sets with images. Latest
set has over 110,000 characters, each with a unique name and identification number
The characters are divided into 8-bit sets called planes. the first 256 planes are the basic
multilingual planes.'''

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    # print('value = "{}", name = "{}", value2 = "{}"'.format(value, name, value2))
    print('value = {}, name = {}, value2 = {}'.format(value, name, value2))

unicode_test(u'A')

unicode_test(u'$')

#below line may not work in Pycharm IDE / Other IDE consoles,
#it works in python console
# unicode_test(u'\u00A2')

