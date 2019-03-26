'''
Created on 19.02.2019 �.

@author: PC1216
'''
def fib(n):
    a, b = 0, 1
    while a < n :
       print(a, end=' ')
       a, b = b, a+b
    print()
fib(1000) 

fruits = ['banana', 'orange', 'lemon']
upper_fruits = [fruit.upper() for fruit in fruits]
print(fruits)
print(upper_fruits)
print(list(enumerate(fruits)))

print(17/3)
print(17//3)
print(17%3)
print(2**3)

a = input('Enter number: ')
b = input('Enter another number:')
num1 = int(a)
num2 = int(b)
print(num1/num2)