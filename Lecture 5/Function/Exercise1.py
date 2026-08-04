def is_armstrong_number(num):
    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Initialize total to 0
    total = 0
    
    # For each digit in the string representation of the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of num_digits
        total += int(digit) ** num_digits
    
    # Check if the total is equal to the original number
    return total == num

print(is_armstrong_number(153))  # True
print(is_armstrong_number(9474))  # True
print(is_armstrong_number(123))  # False