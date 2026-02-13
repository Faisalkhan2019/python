# while True:
#     name = input("Enter name ")
#     n = int(input("What's n? "))
#     if n > 0:
#         break


# for i in range(n):
#     print(f"{name}")


# ---- Example 2

# def main():
#     hello(3)

# def hello(n):
#     for _ in range(n):
#         print("Faisal")
# main()


# ---- Example 3

# def main():
#     number = get_number()
#     hello(number)

# def get_number():
#         while True:
#             n = int(input("What is n? "))
#             if n > 0:
#                 break
#         return n

# def hello(n):
#      for _ in range(n):
#           print("Khan")
# main()



# ------------------------------------------------------
# EXAMPLE 1 – Using while loop with input validation
# ------------------------------------------------------

# while True:
#     name = input("Enter name ")       
#     # OUTPUT (example input): Faisal
#
#     n = int(input("What's n? "))      
#     # OUTPUT (example input): 3
#
#     if n > 0:                         
#         break                        
#
# for i in range(n):                   
#     print(f"{name}")                 
#
# OUTPUT:
# Faisal
# Faisal
# Faisal


# ------------------------------------------------------
# EXAMPLE 2 – Using functions
# ------------------------------------------------------

# def main():
#     hello(3)                         
#
# def hello(n):
#     for _ in range(n):               
#         print("Faisal")              
#
# main()

# OUTPUT:
# Faisal
# Faisal
# Faisal


# ------------------------------------------------------
# EXAMPLE 3 – Full program with user input + functions
# ------------------------------------------------------

# def main():
#     # This function controls the flow of the program

#     number = get_number()   
#     # Example user input: 4

#     hello(number)          


# def get_number():
#     # This function keeps asking until user enters a positive number

#     while True:
#         n = int(input("What is n? "))   
#         # Example input: 4

#         if n > 0:                      
#             break                     

#     return n                           


# def hello(n):
#     # This function prints "Khan" n times

#     for _ in range(n):                 
#         print("Khan")                  


# main()

# # OUTPUT (if user enters 4):
# # Khan
# # Khan
# # Khan
# # Khan


# ------------------------------------------------------
# STUDENT GRADING SYSTEM
# ------------------------------------------------------

# Taking score input from the user
score = int(input("Enter your score: "))
# Example input:
# Enter your score: 85


# We use if / elif / else to check ranges of marks
# The program checks conditions from top to bottom

if score >= 90:
    result = "Excellent"     # 90 or above
elif score >= 80:
    result = "Very Good"     # 80 to 89
elif score >= 70:
    result = "Good"          # 70 to 79
else:
    result = "Fail"          # below 70

# Print the result
print(result)


# ------------------------------------------------------
# Example Outputs
# ------------------------------------------------------

# If user enters: 95
# OUTPUT:
# Excellent

# If user enters: 85
# OUTPUT:
# Very Good

# If user enters: 75
# OUTPUT:
# Good

# If user enters: 50
# OUTPUT:
# Fail
