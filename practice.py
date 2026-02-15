# Practice for List


lists = ["Lahore", "Karachi", "Islamabad", "Peshawar", "faisal"]


# Accessing Items

# print(f"Found a City {lists[-1].title()}")
city = f"We found the City {lists[2].title()}"
# print(city)


# Changing, Adding, and Removing Elements

# Changing item

motors = ["Honda", "Yamaha", "Road Prince", "Suzuki"]
motors[1] = "Toyota"
# print(motors)

# adding elements to a list using append() method

# motors.append("YBR")
# print(f" List of Motor {motors}") #['Honda', 'Toyota', 'Road Prince', 'Suzuki', 'YBR']

# you can start with an empty list and then add items to the list
# using a series of append() calls

# motor = []
# motor.append("Car")
# motor.append("Toyota")
# motor.append("Honda")
# print(motor) #['Car', 'Toyota', 'Honda']


# Inserting Elements into a List

numbers = [1,2,4,5]
# numbers.insert(0, "Faisal") #['Faisal', 1, 2, 4, 5]
# numbers.insert(1, "Hamdan") #[1, 'Hamdan', 2, 4, 5]
# print(numbers)


# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can
# use the del statement


books = ["Pakistan Studies", "Islamic Studies", "Computer Science"]

# del books[1]
# print(books)

# books.clear()
# print(books)



# Removing Items using pop()
# If you’re unsure whether to use the del statement or the pop() method,
# here’s a simple way to decide: when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method.





# list sort() and reverse() 

new_list = [1,22,3,4,5]
# new_list.sort()
# print(new_list)
new_list.reverse()
# print(new_list)


# sorted() function

# one_list = [255,33,44,55]

# # list_two = sorted(one_list)
# list_two = sorted(one_list)

# print(f"Not Sorted {one_list}")
# print(f"Sorted {list_two}")




# Looping in Lists

# more_data = [200, 100, 400, True, "Faisal"]
# for my_data in more_data:
    # print(my_data)  


cities = ["lahore", "karachi", "Islamabad", "Narowal"]

# for city in cities:
    # print(f"City is: {city.title()}")
# print(f" This {city.title()} is great")


# numbs = [2,1,3,4,35,3]

# # print(numbs.pop(2))
# # print(numbs)

# numbs.remove(3)
# print(numbs)



# Guessing game

# final_number = 9
# number_count = 0
# guess_limit = 3

# while number_count < guess_limit:
#     guess = int(input("Guess: "))
#     number_count +=1
#     if guess == final_number:
#         print("you won it!")
#         break
# else:
#     print("sorry you failed")


# This is a simple number guessing game

# This is the correct number that user has to guess
final_number = 9

# This keeps track of how many guesses the user has used
number_count = 0

# This is the maximum number of attempts allowed
guess_limit = 3


# This while loop runs as long as the user has guesses left
while number_count < guess_limit:

    # Ask the user to enter a number
    guess = int(input("Guess: "))

    # Increase the number of guesses by 1
    number_count += 1

    # Check if the user's guess is correct
    if guess == final_number:
        print("You won it!")   # user guessed correctly
        break                # exit the loop immediately


# The else block runs ONLY if the loop finishes normally
# (meaning break was NOT executed)
else:
    print("Sorry, you failed")   # user did not guess in 3 tries
