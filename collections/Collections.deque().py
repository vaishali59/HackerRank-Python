from collections import deque
d=deque()
for _ in range(int(input())):
    cmd,*args=input().split()
    cmd+="("+','.join(args)+')'
    eval('d.'+cmd)
print(*d)
    
