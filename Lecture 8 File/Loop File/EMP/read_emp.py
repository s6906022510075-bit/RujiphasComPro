with open('Lecture 8 File/Loop File/EMP/emp_record.txt', 'r') as emp_file:
    line = emp_file.readline()
    while line != '':
        emp_data = line.strip().split(',')
        name = emp_data[0]
        age = emp_data[1]
        dept = emp_data[2]
        print(f"Name: {name}")
        print(f"Age: {age}") 
        print(f"Department: {dept}")
        line = emp_file.readline()