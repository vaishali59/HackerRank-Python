#find count for repetitions

a=[1,2,1,3,4,1,2]

count={}

for i in a:
    count[i]=count.get(i,0)+1

print(count)
