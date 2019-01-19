#Q.
"""
You have a record of  students.
Each record contains the
student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer  followed by
the names and marks for students. You are required to save the record in a
dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student,
correct to two decimal places.

Input Format

The first line contains the integer , the number of students.
The next  lines contains the name and marks obtained by that student
separated by a space. The final line contains the name of a particular
student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student
correct to 2 decimal places.
"""

student_marks={}
for i in range(int(input("Total Students: "))):
    name, *line = input("Name and respective scores in PCM").split(' ')
    scores = list(map(float,line))
    student_marks[name] = scores
query_name=input("Query Name: ")
print(student_marks)
print(*("%.2f"%(sum(scores)/float(3)) for name,scores in student_marks.items() if name==query_name))
'''
for name,scores in marksheet.items():
    if name==query_name:
        print(sum(scores))
        d=sum(scores)/float(3)
        print("",d)
'''   
