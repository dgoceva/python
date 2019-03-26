'''
Created on 26.02.2019 г.

@author: PC1216
'''
intdata = 1234
floatdata = 1.2345e-3
complexdata = 5+7j

print(type(intdata))
print(type(floatdata))
print(type(complexdata))

print(intdata+345)
print(floatdata-1.6e-3)  #1.6*10**-3
print(complexdata+2+3j)

print(int(3.5))
print(float(6))
print(int('4'))
print(int(float('3.5')))

print('hello '+str(intdata))

text = '    Hello,World!    '
print(text)
print(text[1])
print(text[2:6])
print(len(text))
print(len(text.strip()))
text = '******Hello,**World!    !'
print(text)
print(text.strip('*'))
print(text.replace('*', ''))
print(text.replace(' ', ''))
print(text.upper())
print(text.islower())
print(text.isalpha())
print(text.lower().islower())
print(text.split('!'))
print(len(text.split('!')))

print('Enter a text: ')
txt = input()
print(txt)
print(txt.upper())
txt = input('Enter a text too: ')
print(txt)
num1 = float(input('Enter number 1:'))
num2 = float(input('Enter number 2:'))
print('Result: ',num1+num2)

array = [1,2,3,4,5]
print(array)
print(array[3])
array.sort(reverse=True)
print(array)
array[3] = 'sample'
print(array)
print(len(array))
