try:
    numerator = float(input("enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"the result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

finally:
    print("Execution completed, whether an exception occurred or not.")

print("End of program")