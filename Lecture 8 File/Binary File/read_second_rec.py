import struct   

record_format = 'i20sif'  # Format: name (20 bytes), age (int), department (20 bytes)
record_size = struct.calcsize(record_format)
with open('Lecture 8 File/Binary File/record.bin', 'rb') as file:
    # skip the first record
    file.seek(record_size)  # Move to the second record
    data = file.read(record_size) #read the second record
    record = struct.unpack(record_format, data) #unpack the binary data into a record using struct
    record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
    print(f"ID: {record[0]}")
    print(f"Name: {record[1]}")
    print(f"Age: {record[2]}")
    print(f"GPA: {record[3]}")