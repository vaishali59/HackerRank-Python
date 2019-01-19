from collections import Counter

a=[1,5,3]
s1={3,1}
s2={5,7}

a=Counter(a)
happi=0
for i in a:
    if i in s1:
        happi+=a[i]
    elif i in s2:
        happi-=a[i]
    else:
        pass
print(happi)
