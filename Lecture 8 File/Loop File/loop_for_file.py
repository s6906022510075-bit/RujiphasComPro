with open('Lecture 8 File/Loop File/hello2.txt', 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())
