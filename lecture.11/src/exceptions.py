'''
Created on 7.05.2019 г.

@author: PC1216
'''
a1 = 3

# try:
#     a = int(input('Input a: '))
#     b = eval(input('Input b: '))
#     print(a/b)
# except(ValueError):
#     print('Enter a whole number!')
# except(NameError):
#     print('No such variable!')
# except(ZeroDivisionError):
#     pass
# 
# a = int(input('Input a: '))
# b = eval(input('Input b: '))
# print(a/b)

import sys
# try:
#     f = open('exceptions.py')
#     txt = f.readlines()
#     size = len(txt)
#     f.close()
#     print(size)
#     print(txt)
# except OSError as err:
#     print('OS Error! '+format(err))
    
for f_name in sys.argv[1:]:
    try:
        f = open(f_name)
        size = len(f.readlines())
        print('File {0} has {1} lines'.format(f_name,size))
    except OSError as err:
        print(format(err))
    except:
        pass
