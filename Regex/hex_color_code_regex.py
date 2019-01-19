import re
num=[]
regex = re.compile(r'(?<{.*)#[0-9a-f]{3,6}(?=.*})',re.I)
for _ in range(int(input())):
    num.append((regex.findall(input()))
print(*num,sep='\n')





import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]


N = int(input())
for _ in range(N):
    line = input().strip()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', line, re.I)]
    for code in codes:
        print code
