# def fnction():
#     print "Hello this is Aneesh"
#     return False
#
#
# print(fnction())
#
# # assert 1 == 1
#
# def printsomething(passstring):
#     print(passstring)
#
# printsomething('Aneesh')
#

def checkpalindrome(input_str):
    return (input_str[::-1] == input_str)


def check_func_argument(ip_str_list , replace_str):
    ip_str_list.remove(replace_str)
    return ip_str_list

def str_mut(input_str, replace_str):
    input_str = list(input_str)
    input_str.remove(replace_str)
    return ''.join(input_str)

input_var_str = 'The world is pythonic'
ip_str_list_from_main = list(input_var_str)

# print(ip_str_list_from_main)
print('Passing into function...')

print(ip_str_list_from_main)
print(check_func_argument(ip_str_list_from_main,'n'))
print(ip_str_list_from_main)
print(''.join(ip_str_list_from_main))

print('*'*30)
print('Original string' , input_var_str)
print('modified string ' , str_mut(input_var_str,'n'))
print('Original string' , input_var_str)


# print(checkpalindrome('aha'))
# print(input_var_str)

