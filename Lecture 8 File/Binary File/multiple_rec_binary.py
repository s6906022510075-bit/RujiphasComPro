import struct

#Get the number of records to create from the user
num_records = int(input("How many records do you want to create?: "))
#Open the binary file in write mode
with open('Lecture 8 File/Binary File/record.bin', 'wb') as file:
    #loop to get the data for each record from the user
    for _ in range(num_records):
        #Get data from the user for each record
        id_num = int(input("Enter ID number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))
        #Pack the data into binary format using struct
        data = struct.pack('i20sif', id_num, name.encode('utf-8'), age, gpa)
        #write the binary data to the file
        file.write(data)

print(f"{num_records} records have been written to the binary file.")