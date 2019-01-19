X=int(input("X: "))
Y=int(input("Y: "))
Z=int(input("Z: "))
N=int(input("N: "))
"""
result=[]
for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):
            if (i+j+k)!=N:
                
            else:
                pass
"""

l=([i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k!=N)
l=list(l)
print(*set(tuple(i) for i in (sorted(i)for i in l)))


