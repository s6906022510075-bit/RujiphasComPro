#Writing to a file using the 'with' statement
with open('Lecture 8 File/hello.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.\n')