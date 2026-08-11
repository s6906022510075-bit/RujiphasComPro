fruits_with_duplicates = ["apple", "banana", "orange", "apple", "banana"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Updated fruits list after removing 'apple': {fruits_with_duplicates}")
#Output: Updated fruits list after removing 'apple': ['banana', 'orange', 'banana']