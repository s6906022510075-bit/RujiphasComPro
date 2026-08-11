animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f"The index of 'dog' in the animals list is: {first_dog_index}")
#Output: The index of 'dog' in the animals list is: 1

second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The index of the second occurrence of 'dog' in the animals list is: {second_dog_index}")
#Output: The index of the second occurrence of 'dog' in the animals list is: 4

