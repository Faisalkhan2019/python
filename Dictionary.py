
# ------------------------------------------------------
# PYTHON DICTIONARY
# ------------------------------------------------------
# Dictionary stores data in key:value format
# Used for real-world data (user, product, student)


student ={
    "id": 100,
    "roll_num": 102,
    "class": "MIT",
    "subject": "computer"
}

# accessing key
# print(student["roll_num"])

# method 2 for access key using get()
# print(student.get('roll_num'))
# print(student.get("Uni", "Not found")) # Not found
# print(student.get("Uni")) # None



# print(student.keys())
# print(student.values())

# adding new key and value
# student["Uni"] = "Virtual University"


# changing value
# student["Uni"] = "Punjab University"


# remove key
# student.pop("class")
# print(student)


# copy() the complete dictionary
# new_students = student.copy()

# print(student)
# new_students["city"] = "Lahore"
# print(new_students)


# looping on dictionary

# for my_loop in student:
#     # print(my_loop, ":", student[my_loop])
#     print(f"{my_loop}: {student[my_loop]}")

# star = 0
# while star < 10:
#     print('*'*star)
#     star +=1



# set default value
student.setdefault("Grade", "Excellent")
print(student)



# ========================================================
# PYTHON DICTIONARY – FULLY EXPLAINED NOTES
# ========================================================

# A dictionary is used to store data in KEY : VALUE format.
# It is mostly used for real-world data like:
# student, product, user, account, profile, etc.

# Example:
# {
#    "name": "Faisal",
#    "age": 25,
#    "city": "Lahore"
# }

# # --------------------------------------------------------
# # 1) Creating a Dictionary
# # --------------------------------------------------------

# student = {
#     "id": 100,
#     "roll_num": 102,
#     "class": "MIT",
#     "subject": "computer"
# }

# print(student)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'class': 'MIT', 'subject': 'computer'}

# # --------------------------------------------------------
# # 2) Accessing Values
# # --------------------------------------------------------

# print(student["roll_num"])

# OUTPUT:
# 102

# Using get() method (safe way)

# print(student.get("roll_num"))

# OUTPUT:
# 102

# If key does not exist

# print(student.get("Uni", "Not found"))

# OUTPUT:
# Not found

# print(student.get("Uni"))

# OUTPUT:
# None

# --------------------------------------------------------
# 3) Getting All Keys and Values
# --------------------------------------------------------

# print(student.keys())

# OUTPUT:
# dict_keys(['id', 'roll_num', 'class', 'subject'])

# print(student.values())

# OUTPUT:
# dict_values([100, 102, 'MIT', 'computer'])

# --------------------------------------------------------
# 4) Adding New Data
# --------------------------------------------------------

# student["Uni"] = "Virtual University"
# print(student)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'class': 'MIT', 'subject': 'computer', 'Uni': 'Virtual University'}

# --------------------------------------------------------
# 5) Changing Data
# --------------------------------------------------------

# student["Uni"] = "Punjab University"
# print(student)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'class': 'MIT', 'subject': 'computer', 'Uni': 'Punjab University'}

# --------------------------------------------------------
# 6) Removing Data
# --------------------------------------------------------

# student.pop("class")
# print(student)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'subject': 'computer', 'Uni': 'Punjab University'}

# --------------------------------------------------------
# 7) Copying a Dictionary
# --------------------------------------------------------

# new_students = student.copy()

# new_students["city"] = "Lahore"

# print(student)
# print(new_students)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'subject': 'computer', 'Uni': 'Punjab University'}
# {'id': 100, 'roll_num': 102, 'subject': 'computer', 'Uni': 'Punjab University', 'city': 'Lahore'}

# --------------------------------------------------------
# 8) Looping Through Dictionary
# --------------------------------------------------------

# for key in student:
#     print(key, ":", student[key])

# OUTPUT:
# id : 100
# roll_num : 102
# subject : computer
# Uni : Punjab University

# --------------------------------------------------------
# 9) setdefault() Method
# --------------------------------------------------------

# student.setdefault("Grade", "Excellent")
# print(student)

# OUTPUT:
# {'id': 100, 'roll_num': 102, 'subject': 'computer', 'Uni': 'Punjab University', 'Grade': 'Excellent'}

# If "Grade" already exists, it will NOT change the value.

# --------------------------------------------------------
# 10) Why Dictionary is Important?
# --------------------------------------------------------

# Dictionaries are used in:
# • Login systems
# • User profiles
# • Product systems
# • API data
# • JSON data
# • Database records

# Example:
# user = {
#    "username": "faisal",
#    "password": "1234",
#    "email": "abc@gmail.com"
# }


# # END
# # ========================================================