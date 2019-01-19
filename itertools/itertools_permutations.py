from itertools import permutations
s,k=input().split()
[print(''.join(l)) for l in sorted(list(permutations(s,int(k))))]
