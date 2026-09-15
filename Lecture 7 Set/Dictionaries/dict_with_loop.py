student = {"name" : "Alice", "age" : 25 , "grade" : "A" , "major" : "Computer Science"}

for key in student:
    print(f"{key} : {student[key]}")

#Example 2
student = {"name" : "Alice", "age" : 25 , "grade" : "A" , "major" : "Computer Science"}
for value in student.values():
    print(value)

#Output:
#Alice
#25
#A
#Computer Science

#Example 3
student = {"name" : "Alice", "age" : 25 , "grade" : "A" , "major" : "Computer Science"}


for key, value in student.item():
    print(f"{key} : {value}")