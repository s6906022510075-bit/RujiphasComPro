with open('Lecture 8 File/Loop File/Sale/sales.txt', 'r') as sales_file:
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(format(amount, '.2f'))
        line = sales_file.readline()