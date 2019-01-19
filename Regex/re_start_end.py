import re

S=input()
k=input()
r=re.compile(k)
m=r.search(S)
if not m:print('(-1,-1)')
while m:
    print((m.start(),m.end()-1))
    m=r.search(S,m.start()+1)




'''
print(r.findall(S))
print(match for match in r.finditer(S))


pattern = re.compile(k)
r = pattern.search(S)
if not r: print "(-1, -1)"
while r:
    print "({0}, {1})".format(r.start(), r.end() - 1)
    r = pattern.search(S,r.start() + 1)

'''





    


