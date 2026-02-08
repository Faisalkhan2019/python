# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.



my_list = ["School", "College", "University", "Lahore", "Shahdara"]
# print(my_list[:2]) # getting first two values from the list
print(my_list[3:])  
# print(my_list[-1]) # getting last value from the list

# changing list of any value 
# my_list[0]  = "Faisal" #changed any elment value
# print(my_list) 

# slicing 
# my_list[0:3] = "Khan"
# print(my_list) # ['K', 'h', 'a', 'n', 'Lahore', 'Shahdara']

# my_list[0:2] = ["Addition"]
# print(my_list) #['Addition', 'University', 'Lahore', 'Shahdara']


# splicing

# my_list[1:1] = ["Test", "test"]

# my_list[1:1] =[] #deletion process
# print(my_list)



# looping on Python List like Javascript

# for book in my_list:
#     print(book)
#     print(book, end="-") # this is adding '-' to the each element of the list

# if "Narowal" in my_list:
#     print("Yes Narowal is exist in the list")
# else:
#     print("could not found Narowal")


# my_list.append("Narowal") #append() method same like JS push()
# print(my_list)

# append("add value")
# pop()
# remove("Lahore")
# insert(2, "Mall Road")
# copy()

# squared_num = [x**2 for x in range(10)]
# print(squared_num) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# cube = [x**3 for x in range(10)]
# print(cube)



# ------Compiled by chatGTP

# ======================================================
# PYTHON LISTS – FULLY EXPLAINED NOTES
# ======================================================
# A list is used to store multiple values in one variable.
# Example: storing cities, students, products, marks, etc.

# Python has 4 main collection types:
# List      → ordered, changeable, allows duplicates
# Tuple     → ordered, NOT changeable
# Set       → unordered, unique values
# Dictionary → key-value pairs

# ------------------------------------------------------
# 1) CREATING A LIST
# ------------------------------------------------------

my_list = ["School", "College", "University", "Lahore", "Shahdara"]

print(my_list)
# Output: ['School', 'College', 'University', 'Lahore', 'Shahdara']


# ------------------------------------------------------
# 2) ACCESSING LIST ITEMS
# ------------------------------------------------------

print(my_list[0])      # First item → School
# Output: School

print(my_list[-1])     # Last item → Shahdara
# Output: Shahdara

# Slicing (getting part of list)
print(my_list[:2])     # First two items
# Output: ['School', 'College']

print(my_list[2:])     # From index 2 to end
# Output: ['University', 'Lahore', 'Shahdara']

print(my_list[1:4])    # From index 1 to 3
# Output: ['College', 'University', 'Lahore']


# ------------------------------------------------------
# 3) CHANGING LIST ITEMS
# ------------------------------------------------------

# Change a single item
my_list[0] = "Faisal"
print(my_list)
# Output: ['Faisal', 'College', 'University', 'Lahore', 'Shahdara']

# Change multiple items using slicing
my_list[1:3] = ["Add", "Remove"]
print(my_list)
# Output: ['Faisal', 'Add', 'Remove', 'Lahore', 'Shahdara']


# ------------------------------------------------------
# 4) INSERTING & DELETING USING SLICING
# ------------------------------------------------------

# Insert items at index 1
my_list[1:1] = ["Test", "Demo"]
print(my_list)
# Output: ['Faisal', 'Test', 'Demo', 'Add', 'Remove', 'Lahore', 'Shahdara']

# Delete items using slicing
my_list[1:3] = []
print(my_list)
# Output: ['Faisal', 'Add', 'Remove', 'Lahore', 'Shahdara']


# ------------------------------------------------------
# 5) LOOPING THROUGH A LIST
# ------------------------------------------------------

for item in my_list:
    print(item)

# Output:
# Faisal
# Add
# Remove
# Lahore
# Shahdara

# Print items in one line
for item in my_list:
    print(item, end=" | ")
# Output: Faisal | Add | Remove | Lahore | Shahdara |


# ------------------------------------------------------
# 6) CHECK IF ITEM EXISTS
# ------------------------------------------------------

if "Lahore" in my_list:
    print("Lahore exists in the list")
else:
    print("Lahore not found")

# Output: Lahore exists in the list


# ------------------------------------------------------
# 7) ADDING & REMOVING ITEMS
# ------------------------------------------------------

my_list.append("Narowal")    # add at the end
print(my_list)
# Output: ['Faisal', 'Add', 'Remove', 'Lahore', 'Shahdara', 'Narowal']

my_list.insert(2, "Mall Road")   # add at specific index
print(my_list)
# Output: ['Faisal', 'Add', 'Mall Road', 'Remove', 'Lahore', 'Shahdara', 'Narowal']

my_list.remove("Narowal")    # remove by value
print(my_list)
# Output: ['Faisal', 'Add', 'Mall Road', 'Remove', 'Lahore', 'Shahdara']

last_item = my_list.pop()   # remove last item
print("Removed:", last_item)
# Output: Removed: Shahdara

# Clear the entire list
# my_list.clear()


# ------------------------------------------------------
# 8) LIST INFORMATION
# ------------------------------------------------------

print(len(my_list))         # number of items
# Output: 5

print(my_list.index("Lahore"))   # index of Lahore
# Output: 4

print(my_list.count("Lahore"))   # how many times Lahore appears
# Output: 1


# ------------------------------------------------------
# 9) SORTING & REVERSING
# ------------------------------------------------------

my_list.sort()      # sort alphabetically
print(my_list)
# Output: ['Add', 'Faisal', 'Lahore', 'Mall Road', 'Remove']

my_list.reverse()   # reverse order
print(my_list)
# Output: ['Remove', 'Mall Road', 'Lahore', 'Faisal', 'Add']


# ------------------------------------------------------
# 10) COPYING A LIST
# ------------------------------------------------------

copy_list = my_list.copy()
print(copy_list)
# Output: ['Remove', 'Mall Road', 'Lahore', 'Faisal', 'Add']


# ------------------------------------------------------
# 11) LIST COMPREHENSION (VERY IMPORTANT)
# ------------------------------------------------------
# Used to create lists quickly using loops

# Squares
squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Cubes
cubes = [x**3 for x in range(10)]
print(cubes)
# Output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Only even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# ------------------------------------------------------
# 12) LIST UNPACKING
# ------------------------------------------------------

students = ["Ali", "Ahmed", "Faisal"]

a, b, c = students
print(a)
# Output: Ali
print(b)
# Output: Ahmed
print(c)
# Output: Faisal
