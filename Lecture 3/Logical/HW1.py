print("Please select an option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter your choice (1-4): ")
print("You selected option:", choice)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = num1 + num2
    print("The result of addition is:", result)
elif choice == '2':
    result = num1 - num2
    print("The result of subtraction is:", result)
elif choice == '3':
    result = num1 * num2
    print("The result of multiplication is:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
else:
        print("Error: Invalid choice.")