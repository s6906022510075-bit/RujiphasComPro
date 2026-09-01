num_emps = int(input("How many employees do you want to enter: "))
with open('Lecture 8 File/Loop File/EMP/emp_record.txt', 'w') as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter details for employee #', count, sep='')
        name = input("Name: ")
        id_number = input("ID Number: ")
        dept = input("Department: ")

        emp_file.write(name + '\n')
        emp_file.write(id_number + '\n')
        emp_file.write(dept + '\n')
        print()  # Print a blank line for spacing

print("Employee records have been written to emp_record.txt")