# TRUTHY VS FALSY

# Falsy values include 0, [], {}, (,), False, ""
# I forgot None, 0.0, 0j, set(), range(0)

# YES? NO? PART 1 - technically did not need ' == 1'

# import random
# random_number = random.randint(0, 1)

# if random_number:
#     print("Yes!")
# else:
#     print("No.")

# YES? NO? PART 2 - I got ternary expression confused with a 
# list comprehension.

# my_ternary = "Yes!" if random_number else "No."

# print(my_ternary)

# CHECK THE WEATHER, PART 1

weather = 'sunny'

# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print("Grab your umbrella.")
# else:
#     print("Let's stay inside.")

# MATCH-CASE - I got this right, but this doesn't work on my version 
# of python (3.9). This is valid in version 3.10+.

# animal = 'horse'

# match animal:
#     case 'duck':
#         print('quack')
#     case 'squirrel':
#         print('nook nook')
#     case 'horse':
#         print('neigh')
#     case 'bird':
#         print('tweet tweet')
#     case _:
#         print('*cricket*')

# CHECK THE WEATHER, PART 2

# match weather:
#     case 'sunny':
#         print("It's a beautiful day!")
#     case 'rainy':
#         print("Grab your umbrella.")
#     case _:
#         print("Let's stay inside. ")

# LOGICAL CONDITIONS 1

# if False or True:
#     print('Yes!')
# else:
#     print('No...')
    
# My prediction is that this will print Yes! - accurate

# LOGICAL CONDITIONS 2

# if True and False:
#     print('Yes!')
# else:
#     print('No...')

# This will print "No..." because and requires two truthy statements 
# to be true.

# LOGICAL CONDITIONS 3

# sale = True
# admission_price = 5.25 if not sale else 3.99

# print(f"${admission_price}")

# Prediction - 3.99 because the if statement evaluates to 
# if (False) - accurate

# ARE WE MOVING?

# speed = 0
# acceleration = 24
# braking_force = 19
# is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# print(is_moving)

# prediction: this will print true because this evaluates to 
# true and (false or true). Parenthesis were needed because after 
# the first comparison was evaluated as true, the second 
# expression evaluated would be "true and speed > 0" which is not the 
# order we want to evaluate. 