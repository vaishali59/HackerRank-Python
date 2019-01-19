int(input())
l=input().split()
print(all([all(int(i)>0 for i in l),any(i[::-1] == i for i in l)]))
