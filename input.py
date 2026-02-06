# what is input in Python 
# The input() function in Python is a built-in function used to receive input from a user during program execution

# input() = A function that prompts the user to enter data 
#  Returns the entered data as a string

# ----Let's start ----


# name = input("Enter you name: ") # taking input as a string here
# print(f"Hey {name} how are you?") 

# taking two numbers as a input

# num1 = input("enter number 1: ")
# num2 = input ("enter number 2: ")

# print(f"{num1} + {num2} = {int(num1) + int(num2)}") # output: 2 + 2 = 4  
# print(f"{num1} + {num2} = {int(num1) + int(num2)}") # output: 2 + 2 = 4  


#---- practice ----

# your_name = input("What is your name: ")
# residence  = input ("where you liv: ")
# phone = input("What your phone: ")
# color = input("What your favorite color: ")

# print("\n============OutPut============\n")
# print(f"Your name is: {your_name}")
# print(f"You you live in: {residence}")
# print(f"your phone number is: {phone}")
# print(f"your favorite color is: {color}")

#---- practice ----

# age = int(input("what is your age: "))
# age = age +1
# age += age
# age += 1
# age = input("What is your Age:? ")
# age = int(age) #typecasting
# age = age +1
# print(f"your age is: {age} ")

#---- practice ----

# length = float(input("Enter the length: "))
# width = float(input("Enter the Width: "))

# area = length * width

# print(f"The area is: {area}cm")



#---- Shopping cart program ----

# items = input("What item would you like to buy? ")
# price = float(input("What is the price: "))
# quantity = int(input("How many would you like: "))

# total = price * quantity

# print(f"You have bought {quantity} x {items}'s ")
# print(f"Your total is: ${total}")



# MadLib Game

adjuctive1 = input("Enter an adjuctive: ")
noun1 = input("Enter a noun (perons, place, thing) ")
adjuctive2 = input("Enter an adjuctive: ")
verb = input("Enter verb ending with 'ing'")
adjuctive3 = input("Enter an adjuctive: ")

print(f"Today I went to a {adjuctive1} zoo")
print(f"In a exhibit, I saw a {noun1}")
print(f"{noun1} was a {adjuctive2} and {verb}")
print(f"I was {adjuctive3}")