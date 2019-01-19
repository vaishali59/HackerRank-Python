n,m=map(int,input().split())
data=[]
for _ in range(n):
    data+=map(int,input().split())
    
k=int(input())
for x in sorted(data, key=lambda x:x[k]):
    print(x)



N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)



from operator import itemgetter
N, M = map(int, input().split())

lst = [[int(i) for i in input().split()] for _ in range(N)]

for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)
    
