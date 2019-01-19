N=input()
height=map(int,input().split())
height=set(height)
print(float(sum(height))/len(height))
