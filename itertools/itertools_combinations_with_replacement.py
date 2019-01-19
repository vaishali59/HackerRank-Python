from itertools import combinations_with_replacement as cwr
s,k=input().split()
[print(''.join(l)) for l in list(cwr(sorted(s),int(k)))]
