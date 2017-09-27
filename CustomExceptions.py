class UpperCaseException(Exception):
    pass
#define a custom exception. its a simple class with no behavior defined

words = ['hello','world', '2017', 'CAp']
words = []
if all():


if any(words):
    print "any = true"
else:
    print "any = false"

for word in words:
    print word,
    if word.isupper():
        raise UpperCaseException(word)
