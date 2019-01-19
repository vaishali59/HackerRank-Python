'''
from collections import Counter, OrderedDict as Odict
import operator
s='aabbbccde'
l=Odict()
l=Counter(s)
print(l)
#l=sorted(l.items(),key=operator.itemgetter(1,0), reverse=True)
[print(*i) for i in sorted(l.items(),key=operator.itemgetter(1,0), reverse=True)]
#print(i for i in l)
'''


from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted('aabbbccde')).most_common(3)]

