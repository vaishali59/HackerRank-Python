n=int(input())
width=len("{:b}".format(n))
print("{:b}".format(n))
print(width)

for i in range(1,n+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


#explaination:
# {0:{width}d} == 0 indicates first argument given
#                 :{width} indicates padding
#                 : d/o/X/b indicates format is decimal or octal or hexa or binary

# LINK 1 : https://www.programiz.com/python-programming/methods/string/format
# LINK 2 : https://pyformat.info/


'''
n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
'''
