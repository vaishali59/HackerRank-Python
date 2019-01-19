A={2,4,5,9}
B={2,4,11,12}

print(*sorted(A.union(B).difference(A.intersection(B))),sep='\n')
