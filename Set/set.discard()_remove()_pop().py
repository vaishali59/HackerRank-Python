n=int(input())
s=set(map(int,input().split()))
N=int(input())
for _ in range(N):
    cmd,num =input().split()
    cmd=cmd+'('+num+')'
    s.eval(cmd)
print(s)
    
