num_days = int(input("for how many days do you have sales: "))
with open('Lecture 8 File/Loop File/Sale/sales.txt', 'w') as sales_file:
    for count in range(num_days):
        sales = float(input(f"Enter sales for day #{count}: "))
        sales_file.write(str(sales) + '\n')

print("Sales data has been written to sales.txt")