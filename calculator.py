oprands = input("Enter operands: (+,-,*,/) ")

num_1 = float(input("Enter 1st number: "))

num_2 = float(input("Enter 2nd number "))

if oprands == "+":
    result = num_1 + num_2
    print(f"Number is: {round(result,3)}")
elif oprands == "-":
    result = num_1 - num_2
    print(f"Number is: {round(result,3)}")
elif oprands == "*":
    result = num_1 * num_2
    print(f"Number is: {round(result,3)}")
elif oprands == "/":
    result = num_1 / num_2
    print(f"Number is: {round(result,3)}")
else:

    print(f"{oprands} is not valid")



# Project 2

operator = input("Enter operator (+, -, *, /): ")
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

# Prevent division by zero
if operator == "/" and num_2 == 0:
    print("Cannot divide by zero")
    exit()

# Perform operation
if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    result = num_1 / num_2
else:
    print("Invalid operator")
    exit()

# round() used to limit decimal places
print(f"Result = {round(result, 3)}")
