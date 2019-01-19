n,x=map(int,input().split())
sub=[]
for _ in range(x):
    sub.append(list(map(float,input().split())))

print(sub)
zipped= list(zip(*sub))

print(*[sum(z)/x for z in zipped],sep='\n')
