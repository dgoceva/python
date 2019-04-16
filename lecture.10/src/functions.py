'''
Created on 16.04.2019 г.

@author: PC1216
'''
def firstFunction():
    """First function to be implemented
    """
    #Another comment
    pass
def multiplication(a=3,b=2):
#    print(a*b)
    return a*b
def fib(n=10):
    result = [0,1]
    a,b=0,1
    for x in range(2,n):
        a,b = b,a+b
        result.append(b)
    return result
def Nfact(N):
    result = 1
    for x in range(2,N+1):
        result *= x
    return result
def createList(a,L=[]):
    L.append(a)
    return L
def createList2(a,L=None):
    if (L==None):
        L=[]
    L.append(a)
    return L
def info(kind,*tuple,**dictionary):
    print(kind)
    print(tuple)
    print(dictionary)
    if kind in tuple:
        print(tuple)
    if kind in dictionary:
        print(dictionary[kind])
def lambdaFunc(x):
    return lambda y:x+y

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
print(firstFunction())
print(firstFunction)
print(multiplication(3,4))
print(fib(10))
print(Nfact(eval(input('Input N: '))))
print(fib())
print(multiplication(b=5))
print(createList(1))
print(createList(2))
print(createList(3))
print(createList2(1))
print(createList2(2))
print(createList2(3))
info('python','programming language',
     'GUI',
     python='programming language',
     csharp='programming language',
     html='GUI')
ff = lambdaFunc(6)
print(ff(4))
print(ff(10))
print(__doc__)
print(firstFunction.__doc__)
print(f('spam'))