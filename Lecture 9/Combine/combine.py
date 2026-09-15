try:
    value = int(input("Enter the number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Pleaase enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowsd. please enter a number.")
else:
    print(f"the result is {result}")
finally:
    print("Execution complete.")