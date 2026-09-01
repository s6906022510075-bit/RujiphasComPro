import struct

#define a record with an integer, a string, an integer, and a float
record = (1, 'John Doe', 20, 3.75)

#open a binary file for writing
with open('Lecture 8 File/Binary File/record.bin', 'wb') as file:
    #pack the record into binary format using struct
    data = struct.pack('i20sif', record[0], record[1].encode('utf-8'), 
                       record[2], record[3])
    #write the binary data to the file
    file.write(data)