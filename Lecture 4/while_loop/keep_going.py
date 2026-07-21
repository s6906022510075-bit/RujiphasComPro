keep_going = 'y'
 
while keep_going == 'y':
    sales = float(input('Enter sales: '))
    comm_rate = 2.5
    commission = sales * comm_rate
    print(f'The commission is: ${commission:.2f}')
    keep_going = input('Do you want to calculate another commission? (y/n): ')