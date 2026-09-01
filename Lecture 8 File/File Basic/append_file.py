#Appending to a file using the 'with' statement
with open('Lecture 8 File/hello.txt', 'a') as file:
    file.write('This line is appended to the file.\n')
    file.write('Appending another line.\n')