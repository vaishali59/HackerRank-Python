a=input()
A=set(input().split())
for i in range(int(input())):
    cmd=input().split()[0]
    #print(cmd)
    eval('A.{0}({1})'.format(cmd,set(input().split())))
    #print(A)
print(sum(map(int,A)))
