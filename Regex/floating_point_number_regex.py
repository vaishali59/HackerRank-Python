import re

for _ in range(int(input())):
    n=input()
    #regex = re.compile(r'+|-\d+\.\d*')
    m=re.search(r'^[+|-]?\d*\.\d+$',n)
    if m:
        if float(n):
            print("True")
        else:
            print("False")
    else:
        print("False")




import re
for _ in range(input()):
	print bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', raw_input()))
'''
