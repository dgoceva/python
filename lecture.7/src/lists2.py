'''
Created on 2.04.2019 г.

@author: PC1216
'''
import colorsys
list11 = []
for x in range(10):
    list11.append(x**2)
print(list11)

list1 = [x**3 for x in range(10)]
print(list1)

print([(x,y) for x in [1,2,3] 
       for y in [1,3,6] if x!=y])
vec = [-4,-2,-1,0,1,2,4]
print([x for x in vec if x>0])
print([abs(x) for x in vec])
print([(x,x**2) for x in vec])

str = ['sample', 'banana', 'demo', 'python']
print([x.upper() for x in str])

elem = [[1,2],[3,4,5],[6,7,8,9]]
flatten = [x for el in elem for x in el]
print(flatten)

from math import pi
print(pi)
print([round(pi,i) for i in range(1,6)])

matrix = [
    [1,2,3,4],
    [5,6,7,8]
    ]
print(matrix)
print([[row[i] for row in matrix] 
       for i in range(4)])

print(list(zip(*matrix)))

print(list11)
del list11[4]
print(list11)
del list11[1:3]
print(list11)
del list11[:]
print(list11)
list11 = [x for x in range(7)]
print(list11)
print((min(list11),max(list11)))

del list11
# print(list11)

tuples = 1,2,3
print(tuples)
print(len(tuples))
tuple = 66,
print(tuple,len(tuple))
tt = ()
print(tt,len(tt))
tt1 = (77,)
print(tt1,len(tt1))
print(tuple+tt1)
all = tuples+tuple+tt1
print(all)
print(all[3:5])
print([i*3 for i in all])
print(all[3:1])

sets = {1,2,3,4,1,2,6,7}
setb = {1,2,6,7,11,12}
print(sets)
print(6 in sets,11 in sets)
print(sets-setb)
print(sets|setb)
print(sets&setb)
print(sets^setb)
seta = {}
print(seta)
#print(sets[6])
print({min(sets),max(sets)})
print(len(sets))

simpleset=sets
print(simpleset)
setc = set('simpleset=sets')
print(setc)
print(list(setc))
from colorama import init,Fore,Back,Style
import sys
from colorama import init,Fore,Back,Style

if sys.stdout.isatty() :
    init(convert=True)
print(Fore.CYAN+'Hello')
print(setc)
print(Style.RESET_ALL)

sys.stdout.write("\033[1;31m")
print('All following prints will be red ...')

from colors import color, red, blue

# common colors
print(red('This is red'))
print(blue('This is blue'))

# colors by name or code
print(color('Print colors by name or code', 'white', '#8a2be2'))
print(setc)
