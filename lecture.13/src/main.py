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

from baseclass import Animal,Cat,Dog,print2
animalObj = Animal('',0)
animalObj.print()
catObj = Cat('angora',34)
#catObj.print()
print2(catObj)
catObj.printInfo()
dogObj = Dog('dog1',22,'Dog')
#dogObj.print()
print2(dogObj)

