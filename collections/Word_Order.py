'''
n words repition aloowed
output is count of n
order should be same
####################
from collections import Counter
from collections import OrderedDict
words=[]
for i in range(int(input())):
    words.append(input())

count_dict=OrderedDict()
count_dict=Counter(words)
print(len(count_dict))
print(*count_dict.values())
'''    
    
from collections import Counter, OrderedDict
d=OrderedDict()
for i in range(int(input())):
    key=input()
    d[key]=d.get(key,0)+1

print(len(d))
print(*d.values())
