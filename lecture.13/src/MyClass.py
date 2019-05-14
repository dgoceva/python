'''
Created on 14.05.2019 г.

@author: PC1216
'''
class FirstClass:
    i=100

class SecondClass:
    def __init__(self,i):
       self.i = i
#     def __init__(self):
#         self.i = 0
            
print(FirstClass().i)
obj = FirstClass()
print(obj)
print(obj.i)
obj.i = obj.i+10
print(obj.i)
x = SecondClass(20)
print(x.i)
obj2 = FirstClass()
print(obj2.i)

class Student:
    __number = 0
    def __init__(self,facNo,name,avMark):
        self.facNo = facNo
        self.name = name
        self.mark = avMark
        self.__calc()
        
    def __calc(self):
        self.__number = self.__number+1
        