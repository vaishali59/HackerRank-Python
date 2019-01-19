n = int (input())
arr = [*map(int, input())]
print(*arr, sep=' ')
print(sorted(list(set(arr)),reverse=True)[1])



