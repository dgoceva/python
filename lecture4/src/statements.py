'''
Created on 5.03.2019 г.

@author: PC1216
'''
import string

a1 = eval(input('ENTER a1: '))

a = eval(input('enter a number: '))
if a==0:
    print('You enter zero!')
elif a<0:
    print('a is negative!')
else:
    print('Your number is OK!',a is a1)
if a>=0 and a1>=0:
    print('The sum of a and a1 is ',a+a1)

i=1
sum=0
while i<=a1:
    sum += i
    i += 1
print('sum is ',sum)
i=0
sum=0
while i<a1:
    b = eval(input('enter {0} data : '.format(i+1)))
    if b<=0:
#        continue
        break
    sum += b
    i += 1
print('new sum is {:4f}'.format(sum))

for x in range(1,10,2):
    print(x,end=' ')
print()
for x in range(10,1,-3):
    print(x,end=', ')
print()
avr=0
for x in range(1,10):
    avr += x
print('Average: ',avr/10) 
for x in 'sample Demo 12!$#':
    if x.isspace():
        continue
    elif not x.isalpha():
        break
    print(x.upper(),end=':')
print('\n',x)

fact=1
N=int(input('Input N '))
for x in range(1,N+1):
    fact *= x
print('{0}!='.format(N),fact)
print(N,'!=',fact)
print(str(N)+'!='+str(fact))

listSample = [3,4,5,'one','two',3.1456]
for x in listSample:
    if type(x) is str:
        for y in x:
            print(y,end=' ')
        print()
    else:
        print(x)
