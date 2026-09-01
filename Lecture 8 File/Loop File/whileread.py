with open('Lecture 8 File/Loop File/hello2.txt', 'r') as infile:
    lines = infile.readlines()
    while lines:
        print(lines.pop(0).strip())