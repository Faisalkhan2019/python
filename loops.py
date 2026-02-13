
# books = ["Islamic Stuides", "Pak Studies", "History", "English", "Urdu", "Math"]

# for book in books:
#     print(book)

    
# num = 1
# while num <= 5:
#     for book in books:
#         print(f"{num}-{book}")
# #    num = num +1
#         num += 1
    

# while loop

# Example 1

# i = 3
# while i !=0:
#     print("Hi")
#     i = i - 1



# Example 2

# x = 1
# while x <= 3:
#     print(x, "Hello")
#     x += 1
    

# Output: print hello 4 times
# Hello
# Hello
# Hello
# Hello


# Example 3

  
    

# Output: print hello 4 times
# Hello
# Hello
# Hello


# ------- Nested while loop 
# var_1 = 1
# while var_1 <4:
#     print(f"hamdan".upper())
#     var_1 +=1
#     var_2 = 1
#     while var_2 < 2:
#         print(f"Khan")
#         var_2 +=1
    


# ------ For Loop ------

# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or any other iterable object, executing a block of code once for each item in the sequence. Unlike loops in some other languages that use an index variable to count, Python's for loop acts more like a "for each" loop, directly assigning the value of the current item to a loop variable. 


# name = ["Faisal", "Hamdan"]
# name = [0,1,2]

# for n in range(3):
    # print("Faisal")
    # print(n)
    # rng = range(5*2)
    # print(list(rng))


# Example 1

# my_list = [1,2,3]
# for c in my_list:
#     print(c)

# Ouput:
# 1
# 2
# 3



# ---- Example 2 

# using range(10, 100, 10)

# for book in range(10, 100, 10): 
#     print(f"{book} Book")

# output:
# 10 Book
# 20 Book
# 30 Book
# 40 Book
# 50 Book
# 60 Book
# 70 Book
# 80 Book
# 90 Book

# ---- Example 3


# books = ["Islamic Studies", "Pak Studies", "Urdu", "English", "Math", "Computer"] 

# for book in books:
#     print(book)

# output:
# Islamic Studies
# Pak Studies
# Urdu
# English
# Math
# Computer



# ---- Example 4 with continue

# for a in range(0, 10):
    
#     if a==5:
#         print(f"Found {a}")
#         continue
#     else:
#         print(a)

# output:
# 0
# 1      
# 2      
# 3      
# 4      
# Found 5
# 6      
# 7      
# 8      
# 9 

# ---- Example 5  with break

# for b in range(1, 5):
#     if b == 4:
#         print(f"we found {b}")
#         break
#     print(b)

# output:
# 1
# 2
# 3
# we found 4


# ---- Example 6  looping on string

# name ="Faisal"

# for my_name in name:
#     print(my_name)

# output:
# F
# a
# i
# s
# a
# l




# ---- Assignments ----

# ---- Table Counter Using while loop 

# table = int(input("Enter Table: "))
# counter = int(input("Enter Counter Limit: "))

# i = 1

# while i <= counter:
#     print(f"{table} x {i} = {table * i}")
#     i += 1





# ---- Table Counter Using For Loop and range() Pro version 

# table = int(input("Enter Table: "))
# counter = int(input("Enter Counter Limit: "))

# for i in range(1, counter + 1):
#     print(f"{table} x {i} = {table * i}")
# 

name = "Faisal\n"
# print(name * 5)

b = ["Faisal"]
# print(b)




# ------------------------------------------------------
# Compile by chatGPT
# ------------------------------------------------------

# ======================================================
# PYTHON LOOPS (WHILE & FOR) – FULLY EXPLAINED
# ======================================================

# A loop is used when we want to repeat some code again and again.
# Python has two main loops:
# 1) while loop → runs while a condition is True
# 2) for loop   → runs for each item in a sequence (list, range, string, etc)


# ------------------------------------------------------
# Example 1 – Looping through a list
# ------------------------------------------------------

# A list of books
books = ["Islamic Studies", "Pak Studies", "History", "English", "Urdu", "Math"]

# "book" will take one value at a time from the list
for book in books:
    print(book)      # Prints each book one by one

# OUTPUT:
# Islamic Studies
# Pak Studies
# History
# English
# Urdu
# Math


# ------------------------------------------------------
# Example 2 – Nested loop with numbering
# ------------------------------------------------------

num = 1   # counter variable

# This while loop runs until num becomes 6
while num <= 5:

    # This for loop goes through all books
    for book in books:
        print(f"{num} - {book}")   # prints number and book name
        num += 1                  # increases number by 1

# OUTPUT (first few lines):
# 1 - Islamic Studies
# 2 - Pak Studies
# 3 - History
# 4 - English
# 5 - Urdu


# ------------------------------------------------------
# WHILE LOOP – Example 1
# ------------------------------------------------------

# i starts from 3
i = 3

# This loop will run while i is NOT 0
while i != 0:
    print("Hi")    # prints Hi
    i = i - 1      # decreases i by 1

# OUTPUT:
# Hi
# Hi
# Hi


# ------------------------------------------------------
# WHILE LOOP – Example 2
# ------------------------------------------------------

x = 1

# Loop runs while x is less than or equal to 3
while x <= 3:
    print(x, "Hello")   # prints number and Hello
    x += 1             # increase x by 1

# OUTPUT:
# 1 Hello
# 2 Hello
# 3 Hello


# ------------------------------------------------------
# NESTED WHILE LOOP
# ------------------------------------------------------

var_1 = 1

# Outer loop
while var_1 < 4:
    print("HAMDAN")   # printed 3 times
    var_1 += 1

    var_2 = 1
    # Inner loop
    while var_2 < 2:
        print("Khan")  # printed once for each HAMDAN
        var_2 += 1

# OUTPUT:
# HAMDAN
# Khan
# HAMDAN
# Khan
# HAMDAN
# Khan


# ------------------------------------------------------
# FOR LOOP – Using a list
# ------------------------------------------------------

my_list = [1, 2, 3]

# c takes each value from my_list
for c in my_list:
    print(c)

# OUTPUT:
# 1
# 2
# 3


# ------------------------------------------------------
# FOR LOOP – Using range(start, stop, step)
# ------------------------------------------------------

# range(10, 100, 10) means:
# start from 10
# stop before 100
# increase by 10 each time

for book in range(10, 100, 10):
    print(f"{book} Book")

# OUTPUT:
# 10 Book
# 20 Book
# 30 Book
# 40 Book
# 50 Book
# 60 Book
# 70 Book
# 80 Book
# 90 Book


# ------------------------------------------------------
# FOR LOOP – Looping over book list
# ------------------------------------------------------

books = ["Islamic Studies", "Pak Studies", "Urdu", "English", "Math", "Computer"]

for book in books:
    print(book)   # prints each subject

# OUTPUT:
# Islamic Studies
# Pak Studies
# Urdu
# English
# Math
# Computer


# ------------------------------------------------------
# FOR LOOP – Using continue
# ------------------------------------------------------

# continue skips the current loop and goes to next

for a in range(0, 10):
    if a == 5:
        print(f"Found {a}")
        continue      # skips printing 5
    print(a)

# OUTPUT:
# 0
# 1
# 2
# 3
# 4
# Found 5
# 6
# 7
# 8
# 9


# ------------------------------------------------------
# FOR LOOP – Using break
# ------------------------------------------------------

# break stops the loop completely

for b in range(1, 5):
    if b == 4:
        print(f"We found {b}")
        break          # loop stops here
    print(b)

# OUTPUT:
# 1
# 2
# 3
# We found 4


# ------------------------------------------------------
# LOOPING OVER A STRING
# ------------------------------------------------------

name = "Faisal"

# A string is also a sequence
# Looping over it gives each character

for letter in name:
    print(letter)

# OUTPUT:
# F
# a
# i
# s
# a
# l


# ------------------------------------------------------
# MULTIPLICATION TABLE USING WHILE LOOP
# ------------------------------------------------------

# table = int(input("Enter Table: "))
# counter = int(input("Enter Counter Limit: "))

# i = 1
# while i <= counter:
#     print(f"{table} x {i} = {table * i}")
#     i += 1


# ------------------------------------------------------
# MULTIPLICATION TABLE USING FOR LOOP
# ------------------------------------------------------

# table = int(input("Enter Table: "))
# counter = int(input("Enter Counter Limit: "))

# for i in range(1, counter + 1):
#     print(f"{table} x {i} = {table * i}")


# ------------------------------------------------------
# STRING MULTIPLICATION
# ------------------------------------------------------

name = "Faisal\n"

# Multiplying a string repeats it
# print(name * 5)

# OUTPUT:
# Faisal
# Faisal
# Faisal
# Faisal
# Faisal


# ------------------------------------------------------
# LIST WITH ONE ITEM
# ------------------------------------------------------

b = ["Faisal"]
# print(b)

# OUTPUT:
# ['Faisal']
