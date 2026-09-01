def example_a_plus_mode():
    # Writing to a file using the 'a+' mode
    with open('Lecture 8 File/Binary File/mode +/example_a_plus.txt', 'a+') as file:
        file.seek(0)  # Move the cursor to the beginning of the file

        content = file.read()
        print('Current content of the file:')
        print(content)

        file.write('Appending line as the end of the file.\n')

        # Move the cursor to the beginning of the file
        file.seek(0)
        updated_content = file.read()
        print('\nUpdated content of the file:')
        print(updated_content)

example_a_plus_mode()