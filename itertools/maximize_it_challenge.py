from itertools import product

k,m=map(int,input().split())
N=[list(map(int,input().split()[1:])) for _ in range(k)]
results = (sum(num**2 for num in numbers) % M for numbers in product(*N))
print(max(results))


#print(list(product(*N)))
#print(N)



