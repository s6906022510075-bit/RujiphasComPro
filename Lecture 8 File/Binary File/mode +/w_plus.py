def example_w_plus():
    # Writing to a file using the 'w+' mode
    with open('Lecture 8 File/Binary File/mode +/example_w_plus.txt', 'w+') as file:
        file.write('this is the first line in the file.\n')
        file.write('This is the second line in the file.\n')
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Read the content of the file
        content = file.read()
        print('Content of the file:')
        print(content)

example_w_plus()