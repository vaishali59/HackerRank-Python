s="abcdcdcdc"
#print(s[0:3])
'''
count=0

for c in range(len(s)-2):
    print(c)
    print(s[c:c+3])
    if s[c:c+3]=="cdc":
        count+=1

print(count)
'''
print(sum(1 for c in range(len(s)-2) if s[c:c+3]=="cdc"))
