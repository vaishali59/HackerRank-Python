'''
s='2221311'
i=0
result=[]
while i in range(len(s)):
    temp=s[i]
    c=1
    k=i+1
    while(k<len(s)):
        if s[k]!=temp:
            break
        c+=1
        k+=1
    result.append((c,int(s[i])))
    i=k
print(*result)
'''

from itertools import groupby
print(*[(len(list(g)),int(k)) for k,g in groupby(input())])





'''
1,2,3,4,5,6,7,8,9,10,11,12   key:x: x//5

1//5=0
2//5=0[1,2,3,4]
3//5=0
4//5=0

5//5=1

aaaabbbccdaaabbb   key x
a
a     a
a
a
'''

    



    
