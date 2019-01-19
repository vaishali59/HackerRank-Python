from collections import defaultdict as dfdict
n,m=map(int,input().split())
d=dfdict(list)
l1=[]
for i in range(n):
    d[input()].append(i+1)

for i in range(m):
    l1=l1+[input()]

for i in l1:
    if i in d:
        print(' '.join(map(str,d[i])))
    else:
        print(-1)
    


"""
Collections:
Counter -> returns dictionary
defaultdict -> define default type
"""
