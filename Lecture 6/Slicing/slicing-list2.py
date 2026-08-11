#Slicing a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Slicing from index 2 to 5 (exclusive)
print(numbers[2:5])  # Output: [2, 3, 4, 5]

#Slicing with a step
print(numbers[1:8:2])  # Output: [1, 3, 5, 7]

#slicing from the beginning to index 4 (exclusive)
print(numbers[:4])  # Output: [0, 1, 2, 3]

#slicing from index 6 to the end of the list
print(numbers[6:])  # Output: [6, 7, 8, 9]