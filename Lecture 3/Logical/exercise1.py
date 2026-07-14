hours = int(input("Enter the number of hours worked: \033[1m"))
pay = int(input("Enter the hourly pay rate: \033[1m"))

#if hours > 40:
#    overtime_hours = hours - 40
   # overtime_pay = overtime_hours * pay * 1.5
   # total_pay = (40 * pay) + overtime_pay
   # print(f"Total pay with overtime: ${total_pay:.2f}")

overtime_hours = max(0, hours - 40)
overtime_pay = overtime_hours * pay * 1.5
total_pay = (min(hours, 40) * pay) + overtime_pay
print(f"Total pay: ${total_pay:.2f}")