from collections import Counter
X=input('No. of shoes:')
size=Counter(map(int,input('size available:').split()))
income=0

for i in range(int(input('No. of customers: '))):
    s,price=map(int,input('size,price').split())
    if size[s]:
        income+=price
        size[s]-=1
    else:
        print('size not available')
print(income)




'''
collections returns a dictionary with keys as elements and count as items
'''
