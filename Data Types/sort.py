l=[1,4,6,3,2]
print(sorted(l))

l=[[1,2],[5,3],[9,1],[3,5]]
print(set(tuple(i) for i in (sorted(i)for i in l)))
