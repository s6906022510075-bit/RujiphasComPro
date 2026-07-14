num_employees = int(input("Enter the number of employees: "))
if num_employees < 50:
    print("The company is small.")
elif num_employees < 250:
    print("The company is medium-sized company.")
elif num_employees >= 250:
    print("The company is a large company.")