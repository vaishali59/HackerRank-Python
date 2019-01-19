# Simple dictionary can change the order of the keys whereas OrderedDict
# keeps it unchanged in the order its is entered at the first place

from collections import OrderedDict as Odict
n=int(input())
d=Odict()
for i in range(n):
    item,price=input().rsplit(' ',1)
    d[item]=d.get(item,0)+int(price)

for item,price in d.items():
    print(item,price)

#{'item_buyed':'quantity'}
#bill_items=Odict()


# The rpartition() method takes a
# string parameter separator that
# separates the string at the last occurrence of it.
