'''
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
'''
letters='abcdefghijklmnopqrstuvwxyz'
n=int(input())
l=[]
for i in range(n):
    s='-'.join(letters[i:n])
    l.append((s[::-1]+s[1:]).center(2*n+3,'-'))
    #print(l)
print('\n'.join(l[:0:-1]+l))

'''
line='abc'
l1='-'.join(line[1:3])
print(l1)
print(l1[1:])
'''
