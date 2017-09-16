# lambda function is a anonymous function expressed as a single statement
# for example , a function to capitalize each word passed into it

stairs = ['hello', 'thud', 'meow', 'hiss']

# print(stairs)

def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):
    '''this function capitalizes the word that is
    passed into it'''
    return word.capitalize() + '!'

edit_story(stairs,enliven)
# note the usage of passing function as an argument into another function
# enliven function passed as an argument to edit_story function
# when you pass a function as argument, parentheses need not be given
# parentheses means its calling the function

edit_story(stairs, lambda word: word.capitalize() + "!")
# above function call uses lambda which means no need to define a formal function
# instead write function on the fly inline
# Best use case of lambda  is when you need tiny / trivial functions without naming hassles
