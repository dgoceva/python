'''
Created on 26.03.2019 г.

@author: PC1216
'''
data = [1,2,3,4,5]
print(data)
var = eval(input('Input new data: '))
data.append(var)
print(data)
data.insert(1, var)
print(data)
newData = [6,7]
print(newData)
newData.extend(data)
print(newData)
newData.remove(7)
print(newData.count(7))
if newData.count(7):
    newData.remove(7)
print(newData)
print(newData.pop(0))
print(newData)
print(newData.pop())
print(newData)
newData.clear()
print(newData)
newData.extend(data)
newData.extend(data)
print(newData)
print(newData.index(3))
newData.reverse()
print(newData)
newData.sort()
print(newData)
newData.sort(reverse=True)
print(newData)
newData.clear()
print(newData)
newData = data.copy()
print(newData)
newData[2] = 77
print(newData)
print(data)

from collections import deque
queue = deque([4,3,2,1])
print(queue)
print(queue.popleft())
print(queue.pop())
print(queue)
queue.append(66)
queue.appendleft(99)
print(queue)