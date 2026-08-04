def calculate_stat(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, average, maximum, minimum = calculate_stat(numbers)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

#Output
#Total: 75
#Average: 15.0
#Maximum: 25
#Minimum: 5
