'''
Created on 14.05.2019 г.

@author: PC1216
'''
import MyClass

y = MyClass.FirstClass()
print(y)
print()

from MyClass import FirstClass,Student
x = FirstClass()
print(x)
st = Student(123,'Ivan Ivanov',5.65)
print(st.facNo,st.name,st.mark)
