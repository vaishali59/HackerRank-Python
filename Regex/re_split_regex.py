import re

print(*re.split(r'[.,]+',input()), sep='\n')
print("\n".join(re.split(r'[,.]+',input())))
