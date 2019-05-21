'''
Created on 21.05.2019 г.

@author: PC1216
'''
with open('baseclass.py','r') as f:
    data = f.read()
    print(data)
    f.close()
    
with open('main.py','r') as f:
    lines = f.readlines()
    f.close()
print(lines[5])

for line in lines:
    if line.find('#')!=-1:
        print(line)

import json
print(json.dumps(lines[5]))
with open('main.json','w') as fp:
    json.dump(lines, fp)
    fp.close()