import struct

# Read multiple records from a binary file
with open('Lecture 8 File/Binary File/record.bin', 'rb') as file:
    # Calculate the size of a single record
    record_size = struct.calcsize('i20sif')
    # Read records until the end of the file
    while True:
        data = file.read(record_size)
        if not data:
            break
        # Unpack the binary data into a record using struct
        record = struct.unpack('i20sif', data)
        # Decode the name from bytes to string and remove any null bytes
        record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
        print(f"ID: {record[0]}")
        print(f"Name: {record[1]}")
        print(f"Age: {record[2]}")
        print(f"GPA: {record[3]}")
