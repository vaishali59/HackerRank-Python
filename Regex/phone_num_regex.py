import re

for _ in range(int(input())):
    m=re.search(r'^[789]\d{9}$',input())
    if m:
        print("YES")
    else:
        print("NO")

