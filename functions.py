# # def fnction():
# #     print "Hello this is Aneesh"
# #     return False
# #
# #
# # print(fnction())
# #
# # # assert 1 == 1
# #
# # def printsomething(passstring):
# #     print(passstring)
# #
# # printsomething('Aneesh')
# #
#
# def checkpalindrome(input_str):
#     return (input_str[::-1] == input_str)
#
#
# def check_func_argument(ip_str_list , replace_str):
#     print('memory address inside function', hex(id(ip_str_list)))
#     ip_str_list.remove(replace_str)
#     return ip_str_list
#
# def str_mut(input_str, replace_str):
#     input_str = list(input_str)
#     input_str.remove(replace_str)
#     return ''.join(input_str)
#
# input_var_str = 'The world is pythonic'
# ip_str_list_from_main = list(input_var_str)
#
# # print(ip_str_list_from_main)
# print('Passing into function...')
#
# print('mem address outside function' , hex(id(ip_str_list_from_main)))
# print('original string list var', ip_str_list_from_main)
# print(check_func_argument(ip_str_list_from_main,'n'))
# print('original string list var', ip_str_list_from_main)
# print('full string using original var', ''.join(ip_str_list_from_main))
# print('mem address outside function' , hex(id(ip_str_list_from_main)))
#
#
# print('*'*30)
# print('Original string' , input_var_str)
# print('modified string ' , str_mut(input_var_str,'n'))
# print('Original string' , input_var_str)
#
# def mutate_number(num):
#     num = num*3
#     return num
#
# n = 10
# print 'original number ', n
# print(mutate_number(n))
# print 'original number ', n
#
#
#
#
#
#
# # print(checkpalindrome('aha'))
# # print(input_var_str)
#
# def check_mem_address_immutable(strinput):
#     print(hex(id(strinput)))
#
#
# a = 'Hello'
# print('mem address outside of function', hex(id(a)))
# check_mem_address_immutable(a)
# print('mem address outside of function', hex(id(a)))
#

# def menu(wine, entree, dessert):
#     return {'wine':wine, 'entree':entree , 'dessert':dessert}
#
# print menu('wine1','ma po tofu','gadbad')
#
# try:
#     pass
#     # print menu('wine1', wine='Merlotwhatever' , entree='thai curry' , dessert='Falooda')
#     # print menu(wine='Merlotwhatever' , entree='thai curry' , dessert='Falooda','wine1' )
# except:
#     print('Error')
#
# def menu1(wine, entree, dessert='Gadbad'):
#     return {'wine':wine, 'entree':entree , 'dessert':dessert}
#
# print(menu1('wine1.' , 'entree1..'))

# def print_args(*args):
#     """this is a function to
#     accept *args and return a tuple of positional parameters.
#     It accepts multiple arguments and prints out a set - removes duplicates
#     -trailing spaces taken care of """
#     print('Positional argument tuple' , set(args))
#     print(dict(zip(range(len(args)), args)))
#
# print_args('Hello','Aneesh', 100,1000,'Hello','Aneesh')
# # print print_args.__doc__

# def print_kwargs(**kwargs):
#     print 'Keyword Arguments', kwargs
#
# print_kwargs(usa = 'dc', india = 'delhi')

# def answer():
#     print(42)
#
# answer()
#
# def call_some_function(func):
#     func()
#
# # answer = 10
# answer()
#
# call_some_function(answer)

def outerfunction():
    def inner_func(a,b):
        print("this is inner function call")
        print ('inner function - sum of {} , {} '.format(a, b), a+b)
        def whatever():
            print "this is a whatever double inner function"
        whatever()
        return (a + b)
    print("this is outer function call")
    inner_func(1,3)
    print inner_func(10,23)

    # return inner_func(01,23)

# print outerfunction()
outerfunction()
