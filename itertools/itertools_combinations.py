from itertools import combinations
s,k=input().split()
for n in range(1,int(k)+1):
    [print(''.join(l)) for l in list(combinations(sorted(s),int(n)))]
    
