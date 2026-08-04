def my_function():
    local_variable = "I am a local variable"
    print(local_variable)

my_function()  # This will print: I am a local variable

#Accessing local_variable outside the function will raise an error
# print(local_variable)  # Uncommenting this line will raise a NameError