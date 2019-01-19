'''
s=c0c1....cn-1
k=k is factor of n i.e n%k==0
t=n/k

each ti segment consists of 

'''

from collections import OrderedDict as ordict
s=input()
k=int(input())
n=len(s)
for i in range(0,n,k):
    t= s[i:i+k]
    print(''.join(ordict.fromkeys(t)))
    
'''
T=('CAA')
u=''.join(set(T))
print(u)
'''


