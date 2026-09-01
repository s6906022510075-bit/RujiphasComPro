import struct

#open the binary file for reading
with open('Lecture 8 File/Binary File/record.bin', 'rb') as file:
    #read the binary data from the file 
    data = file.read(struct.calcsize('i20sif'))
    #unpack the binary data into a record using struct
    record = struct.unpack('i20sif', data)
    #decode the name from bytes to string and remove any null bytes
    record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
    print(f"ID: {record[0]}")
    print(f"Name: {record[1]}")
    print(f"Age: {record[2]}")
    print(f"GPA: {record[3]}")