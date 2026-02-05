
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# school = "Oxford"
# is_student = True

# print(f"Your name is: {name}")
# print("--------------------")
# print(f"Your age is: {age}")
# print("--------------------")
# print(f"Your school is: {school}")
# print("--------------------")
# print(f"Are you Student: {is_student}")

# def main(a, b):
#     return a + b

# print(main(5, 10))
    
# print ("Hello world")

# mix text and numbers

# name = str(input("Enter Your Name "))
# age = int(input("Enter Your Age: $"))
# print(f"Hi {name} your age is {age}")

# print("My name is Faisal", 30, "Age")

# ----- Math Operators ----- 
# print(35%6)
# print(5 ** 5)
# print( 5/2)

x = 4 # this is int
y = "Faisal" # this is str
z = True # this is bool 

# print(3.0-1) # Output: 2.0 

'''
print(f"3 + 2 = {3 + 2}")
print(f"5 - 1 = {5 - 1}")
print(f"3 * 4 = {3 * 4}")
print(f"10 / 5 = {10 / 5}")
print(f"35 % 3 = {35 % 3}")
print(f"2 ** 4 = {2 ** 4}")

a = 1
b = 1.0
z = 1
print(a is b is z)
'''


# ------ Comparison Operators ------
 
# print (5>3 and 2<4) # Output: True
# print (5>3 or 2>4) # Output: True   

# print(5 == 2) 
# print(5 != 2)    
# print(5 >= 1)    
# print(5 == 5)    
# print(5 != 5)    
# print(5 < 10)    
# print(5 <= 5) 


# ------ Variables ------

my_name = "Faisal"

print(my_name)

my_age = 30
# print(f"Age data type is: {type(my_age)}") 



# number convert to string

# my_number = "faisal"
# my_number = bool(my_number)
# print(my_number)
# print(type(my_number))


my_1 = 20
my_2 = "30"
# print(my_1 + my_2)

v_1 = 1
my_v = "faisal"

# print(my_v, v_1)

# ------ FUN WITH MATH AND STRINGS ------

your_name = "Hamdan "

# using + with number and string
# print(your_name + 5) # Output:  will give us TypeError

# using * with string 
# print(your_name * 5) # will print 5 times (Hamdan Hamdan Hamdan Hamdan Hamdan) so this is the different from both of them +, *

# using / with string 
# print (your_name / 5) # Output:  will give us TypeError

# uisng % with string 
# print( your_name % 5) #Output:  will give us TypeError

#using - with string 
# print (your_name - 5) #will give us TypeError





# ----- ASSIGNMENT OPERATORS -----

# = Assigns something from the right to the left
# += Adds and Assigns
# -= Subtracts and Assigns
# *= Multiplies and Assigns
# /= Divides and Assigns
# %= Modulus and Assigns
# **= Exponents and Assigns


# x = 10**2

# # x += 1
# # x **= 2
# print (x)

# x = input("Enter number: ")
# print(int(x) + 10)


number_1 = 14
number_1 = number_1 + 27
print(number_1)


# '''Compiled from ChatGPT'''

# =====================================================
# PYTHON BASICS – FULLY EXPLAINED NOTES
# =====================================================

# -------------------------------
# 1) VARIABLES & DATA TYPES
# -------------------------------

# A variable is a container that stores data

x = 4           # x stores an integer number
y = "Faisal"    # y stores a string (text)
z = True        # z stores a boolean (True or False)

# Python automatically detects the data type
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
print(type(z))   # <class 'bool'>


# -------------------------------
# 2) USER INPUT & OUTPUT
# -------------------------------

# input() always takes data from user as STRING

name = input("Enter your name: ")    # user types name
age = input("Enter your age: ")      # user types age (still string)

# Convert age to integer for calculations
age = int(age)

# f-strings allow mixing text and variables easily
print(f"Your name is: {name}")
print(f"Your age is: {age}")


# -------------------------------
# 3) CONSTANT VALUES
# -------------------------------

# These are normal variables but used as fixed data
school = "Oxford"
is_student = True

print(f"School: {school}")
print(f"Are you a student? {is_student}")


# -------------------------------
# 4) FUNCTIONS
# -------------------------------

# A function is a reusable block of code
# It avoids writing the same code again and again

def add(a, b):          # a and b are parameters
    return a + b       # function returns sum

# Call the function
result = add(5, 10)
print(result)


# -------------------------------
# 5) MATHEMATICAL OPERATORS
# -------------------------------

# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# %  Remainder (modulus)
# ** Power

print(3 + 2)     # 5
print(5 - 1)     # 4
print(3 * 4)     # 12
print(10 / 5)    # 2.0 (always float)
print(35 % 3)    # 2 (remainder)
print(2 ** 4)    # 16


# -------------------------------
# 6) TYPE CONVERSION
# -------------------------------

# Input always returns string
num = "10"

# Convert string to integer
print(int(num) + 5)    # 15

# Convert to boolean
name = "Faisal"
print(bool(name))     # True (because string is not empty)

empty = ""
print(bool(empty))    # False (empty string)


# -------------------------------
# 7) COMPARISON OPERATORS
# -------------------------------

# These return True or False

print(5 == 5)    # equal
print(5 != 2)    # not equal
print(5 > 3)     # greater than
print(5 < 10)    # less than
print(5 >= 5)   # greater or equal
print(5 <= 5)   # less or equal


# -------------------------------
# 8) LOGICAL OPERATORS
# -------------------------------

# and → both conditions must be true
# or  → any one condition can be true

print(5 > 3 and 2 < 4)   # True
print(5 > 3 or 2 > 4)    # True


# -------------------------------
# 9) STRING & NUMBER BEHAVIOR
# -------------------------------

name = "Hamdan"

# Using * with string repeats it
print(name * 3)   # HamdanHamdanHamdan

# These will cause errors
# name + 5     # ❌ cannot add string and number
# name / 2     # ❌ cannot divide string


# -------------------------------
# 10) ASSIGNMENT OPERATORS
# -------------------------------

x = 10

x += 5     # same as x = x + 5
x *= 2     # same as x = x * 2
x **= 2    # same as x = x ** 2

print(x)


# -------------------------------
# 11) USER INPUT WITH MATH
# -------------------------------

number = input("Enter a number: ")
number = int(number)

print(number + 10)


# -------------------------------
# 12) PRACTICE EXAMPLE
# -------------------------------

number_1 = 14
number_1 = number_1 + 27   # adding 27 to existing value
print(number_1)           # 41
