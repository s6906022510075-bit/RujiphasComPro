phonebook = {'Max': '555-1234', 'Alice': '555-5678', 'Bob': '555-8765'}

print(phonebook)  # Output: {'Max': '555-1234', 'Alice': '555-5678', 'Bob': '555-8765'}

print(phonebook['Max'])  # Output: 555-1234
print(phonebook.get('Bob'))  # Output: 555-8765

key_to_check = 'Charlie'
if key_to_check in phonebook:
    print(f"{key_to_check} is in the phonebook.")
else:
    print(f"{key_to_check} is not in the phonebook.")  # Output: Charlie is not in the phonebook.

phonebook['Simpson'] = '555-4321'
phonebook['Charlie'] = '555-0000'
phonebook['Alice'] = '555-9999'
print(phonebook)  # Output: {'Max': '555-1234', 'Alice : '555-9999', 'Bob': '555-8765', 'Simpson': '555-4321', 'Charlie': '555-0000'}

del phonebook['Simpson']
print(phonebook)  # Output: {'Max': '555-1234', 'Alice': '555-9999', 'Bob': '555-8765', 'Charlie': '555-0000'}