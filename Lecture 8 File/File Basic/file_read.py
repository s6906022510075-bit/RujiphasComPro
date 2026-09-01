#This program reads the contents of a file and displays it on the screen.
def main():
    #Open the file named philosopher.txt from the Lecture 8 File directory to read its contents.
    infile = open('Lecture 8 File/philosopher.txt', 'r')

    #Read the contents of the file into a variable
    file_contents = infile.read()

    #Close the file
    infile.close()

    #Display the contents of the file on the screen
    print(file_contents)

#Call the main function
main()