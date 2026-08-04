counter = 0

def increment():
    global counter
    counter += 1

#calling function increment() twice
increment()
increment()

#Accessing the global variable counter
print(counter)  # Output: 2