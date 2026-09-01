#This program writes three lines of text to a file.
def main():
    #Open a file named philosopher.txt from the Lecture 8 File directory to write to it. 
    #If the file does not exist, it will be created.
    outfile = open('Lecture 8 File/philosopher.txt', 'w')

    #Write the names of three philosophers to the file. 
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #Close the file
    outfile.close()

#Call the main function
main()

#w = write, 
# r = read, 
# a = append, 
# r+ = read and write, 
# b = binary, 
# t = text