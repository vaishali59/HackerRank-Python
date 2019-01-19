n,m=map(int,input().split())
pattern=[('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(pattern+['WELCOME'.center(m,'-')]+pattern[::-1]))


'''
l1=[1,1,1]
l2=[2,2,2]
l3=[3,3,3]

print(l1+l2+l3)
'''




















