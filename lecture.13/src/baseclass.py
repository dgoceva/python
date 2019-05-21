'''
Created on 21.05.2019 г.

@author: PC1216
'''
class Animal:
    __number=0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def print(self):
        print('This is base class Animal')
    
    def printInfo(self):
        print('This is sample')

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
        self.typeanimal = 'cat'
        self.__number = 11
    
#     def print(self):
#         print('This is class Cat')
#         print('Name: '+self.name+', Age: '+str(self.age))
#         print('__number: '+str(self.__number))

class Dog(Animal):
    def __init__(self,name,age,typeanimal):
        super().__init__(name, age)
        self.typeanimal = type
        self.__number = 44
    
#     def print(self):
#         print('This is class ',self.type)
#         print('Name: '+self.name+', Age: '+str(self.age))
#         print('__number: '+str(self.__number))

def print2(obj):
        print('This is class ',obj.typeanimal)
        print('Name: '+obj.name+', Age: '+str(obj.age))
    