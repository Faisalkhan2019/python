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