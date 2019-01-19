"""
Given an integer,n , and n space-separated integers as input, create a tuple,t ,
of those n integers. Then compute and print the result of hast(t).

Note: hash(t) is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer,n, denoting the number of elements in the tuple. 
The second line contains n space-separated integers describing the elements in tuple t.
"""
# Method 1
'''
n,*nums = input("No. of intezers and list of integers: ").split()
numbers=tuple(map(int,nums))
print(numbers)
print(hash(numbers))
'''
# Method 2
'''
n = int(input("total no.: "))
nums=(int(input()) for _ in range(n))
print(*nums)
'''
# Method 3
n=int(input("total no. : "))
numlist=tuple(map(int,input("Enter integer list").split()))
print(hash(numlist))
