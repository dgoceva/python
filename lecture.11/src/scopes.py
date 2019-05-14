'''
Created on 14.05.2019 г.

@author: PC1216
'''
def scope_test():
    spam = 'scope_test'
    print(spam)
    
    def inner_test():
        nonlocal spam
        spam = 'inner_test'
        print(spam)
        
    def inner2_test():
        spam = 'inner2_test'
        print(spam)
        
    def inner3_test():
        global spam
        spam = 'inner3_test'
        print(spam)
    print(spam)
    inner_test()
    print(spam)
    inner2_test()
    print(spam)
    inner3_test()
    print(spam)
    
spam = 'global'
scope_test()
#scope_test.inner_test()
print(spam)