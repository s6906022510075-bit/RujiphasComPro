input_string = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    uppercase_char = char.upper()
    if uppercase_char in vowels:
        modified_string += "*"
    else:
        modified_string += uppercase_char
print("Modified string:", modified_string)