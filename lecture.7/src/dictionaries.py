'''
Created on 9.04.2019 г.

@author: PC1216
'''
from audioop import reverse
emp={}
print(emp)
emp = {121:'peter',111:'ivan', 101:'joan',99:'maria'}
print(emp)
print(emp[99])
emp[99]='ivan'
print(emp)
emp[98]='maria'
print(emp)
emp[97]=emp[101]
print(emp)
if 1 in emp:
    emp[96]=emp[1]
print(emp)

math = {x:x**3 for x in range(1,10)}
print(math)

sum=0
for k,v in math.items():
    print(k,v)
    sum += v
print('sum of values: ',sum)

numbers = ['zero','one','two','three','four','five']
for i in enumerate(numbers):
    print(i)
    
text = ''
for k,v in enumerate(numbers):
    print(v)
    text += v+' '
print(text)

print(list(numbers))
print(sorted(numbers))
print(sorted(numbers,reverse=True))
print([x for x in reversed(sorted(numbers))])

print(sorted(emp))
print({k:v for k in reversed(sorted(emp))})

print((1,2,4)>(1,2,3))
print([1,2,4]>[1,2,3])
print({1,2,4}>{1,2,3})
print((1,2,3)==(1.0,2.0,3.0))
#print(gt({1:'one',2:'two',4:'four'},
#          {1:'one',2:'two',3:'three'}))

print(len(emp))
print(str(emp))
print(type(emp))
print(type(numbers))
print(type((1,2,3)))

list=[v for v in enumerate(numbers)]
print(list)
new_list=[]
for i,j in list:
    if i>3:
        new_list.append(j+' ')
        new_list += j+' '
print(new_list)