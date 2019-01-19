n = int(input())
s = set(map(int, input().split()))
print(s)
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
    print(s)
print(sum(s))
