import re

for _ in range(int(input())):
    x,y=input().split()
    regex = re.compile(r'<[a-zA-Z][A-Za-z0-9-_\.]+@[A-Za-z]*\.[A-Za-z]{1,3}>')
    m=regex.search(y)
    if m:
        print(x,y)


'''
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)
'''
