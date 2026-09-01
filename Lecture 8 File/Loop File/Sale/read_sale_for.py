with open('Lecture 8 File/Loop File/Sale/sales.txt', 'r') as sales_file:
    for line in sales_file:
        amount = float(line)
        print(format(amount, '.2f'))