"""
from operator import itemgetter
students=[]
for N in range(1,int(input("Enter max number of students"))+1):
        name = input("Name: ")
        score = float(input("Score: "))
        students.append([name,score])

print(students)
L = sorted(students, key=itemgetter(0))
L1 = tuple(set(tuple(sorted([l[1] for l in students]))))

print(L)
print(L1)    

grade=L1[-2]
print("grade:",grade)
for l in L:
    if l[1]==grade:
        print(l[0])
        print(l[1])

print("{}\{}".format(l[0],l[1]) for l in L if l[1]==grade])
"""

"""
marksheet = []
for _ in range(0,int(input('Total Number'))):
    marksheet.append([input('Name: '), float(input("Score: "))])

print(marksheet)
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

print(sorted(list(set([marks for name,marks in marksheet]))))
print(*("{}\n{}".format(a,b) for a,b in sorted(marksheet) if b==second_highest),sep='\n')
    
"""

print(*('{}\n{}'.format(n,n**2) for n in range(5) if n%2))
#print(l)
