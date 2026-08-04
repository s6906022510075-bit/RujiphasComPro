def format_string(*args):
    # Concatenate all arguments into a single string
    concatenated_string = ''.join(args)
    
    # Convert the concatenated string to uppercase
    uppercased_string = concatenated_string.upper()
    
    return uppercased_string
pass

if __name__ == "__main__":

    result = format_string("Hello", "World" , "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_string("Python", "is", "fun")   
    print(result)  # Output: "PYTHONISFUN"

    result = format_string('Hello', "-", "world")
    print(result)  # Output: "HELLO-WORLD"