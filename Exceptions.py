# making custom exceptions
class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'MINY', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)
        except UppercaseException as e:
            print(e.message)
            continue
