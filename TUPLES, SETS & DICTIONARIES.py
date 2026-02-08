# ======================================================
# PYTHON TUPLES, SETS & DICTIONARIES – FULL NOTES
# ======================================================

# ------------------------------------------------------
# PYTHON TUPLE
# ------------------------------------------------------
# A tuple is like a list BUT it cannot be changed (immutable)
# Used when data should never change (months, days, settings)

# Creating a tuple
my_tuple = ("Ali", "Ahmed", "Faisal")

print(my_tuple)
# Output: ('Ali', 'Ahmed', 'Faisal')

# Accessing tuple items
print(my_tuple[0])
# Output: Ali

print(my_tuple[-1])
# Output: Faisal

# Slicing tuple
print(my_tuple[1:3])
# Output: ('Ahmed', 'Faisal')

# Checking if value exists
print("Ali" in my_tuple)
# Output: True

# Tuple length
print(len(my_tuple))
# Output: 3

# Tuples cannot be changed
# my_tuple[0] = "Hamdan"  ❌ This will give error


# ------------------------------------------------------
# CONVERT TUPLE TO LIST (to modify)
# ------------------------------------------------------

temp = list(my_tuple)
temp.append("Hamdan")
my_tuple = tuple(temp)

print(my_tuple)
# Output: ('Ali', 'Ahmed', 'Faisal', 'Hamdan')


# ------------------------------------------------------
# TUPLE UNPACKING
# ------------------------------------------------------

students = ("Ali", "Ahmed", "Faisal")

a, b, c = students
print(a)
print(b)
print(c)
# Output:
# Ali
# Ahmed
# Faisal


# ------------------------------------------------------
# PYTHON SET
# ------------------------------------------------------
# Set stores unique values (no duplicates)
# Order is NOT guaranteed

my_set = {"Lahore", "Karachi", "Islamabad", "Lahore"}

print(my_set)
# Output: {'Lahore', 'Karachi', 'Islamabad'}

# Add item
my_set.add("Narowal")
print(my_set)
# Output: {'Lahore', 'Karachi', 'Islamabad', 'Narowal'}

# Remove item
my_set.remove("Karachi")
print(my_set)
# Output: {'Lahore', 'Islamabad', 'Narowal'}

# Check item
print("Lahore" in my_set)
# Output: True

# Set length
print(len(my_set))
# Output: 3


# ------------------------------------------------------
# SET OPERATIONS
# ------------------------------------------------------

set1 = {"A", "B", "C"}
set2 = {"B", "C", "D"}

print(set1.union(set2))
# Output: {'A', 'B', 'C', 'D'}

print(set1.intersection(set2))
# Output: {'B', 'C'}

print(set1.difference(set2))
# Output: {'A'}


# ------------------------------------------------------
# PYTHON DICTIONARY
# ------------------------------------------------------
# Dictionary stores data in key:value format
# Used for real-world data (user, product, student)

student = {
    "name": "Faisal",
    "age": 25,
    "city": "Lahore"
}

print(student)
# Output: {'name': 'Faisal', 'age': 25, 'city': 'Lahore'}

# Access value
print(student["name"])
# Output: Faisal

# Using get()
print(student.get("age"))
# Output: 25

# Change value
student["city"] = "Narowal"
print(student)
# Output: {'name': 'Faisal', 'age': 25, 'city': 'Narowal'}

# Add new key
student["course"] = "Python"
print(student)
# Output: {'name': 'Faisal', 'age': 25, 'city': 'Narowal', 'course': 'Python'}

# Remove key
student.pop("age")
print(student)
# Output: {'name': 'Faisal', 'city': 'Narowal', 'course': 'Python'}


# ------------------------------------------------------
# LOOPING THROUGH DICTIONARY
# ------------------------------------------------------

for key in student:
    print(key, ":", student[key])

# Output:
# name : Faisal
# city : Narowal
# course : Python


# ------------------------------------------------------
# DICTIONARY METHODS
# ------------------------------------------------------

print(student.keys())
# Output: dict_keys(['name', 'city', 'course'])

print(student.values())
# Output: dict_values(['Faisal', 'Narowal', 'Python'])

print(student.items())
# Output: dict_items([('name', 'Faisal'), ('city', 'Narowal'), ('course', 'Python')])
