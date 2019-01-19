# Q. what is the difference between iterable and iterator

from itertools import combinations,groupby
'''
N=int(input())
K=int(input())
l1=[k for k,v in enumerate(input().split(),1) if v=='a']
l2=list(combinations(range(1,N+1),K))
count=0
for j in l2:
    if any(x in j for x in l1):
        count+=1
        print(j)
print('%.4f'%(float(count/len(l2))))

'''

N=int(input())
#L=input().split()
#K=int(input())
C=list(combinations(input().split(),int(input())))
print(C)
L=[i for i in C if 'a' in i]
print(L)
print('%.4f'%(float(len(L)/len(C))))
