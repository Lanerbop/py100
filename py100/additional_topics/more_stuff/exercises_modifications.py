# EXERCISE 1

# What does the following function do? Be sure to identify the output value.


# def do_something(dictionary):
#     return tuple(sorted(dictionary.keys())[1].upper())

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict))
# do_something takes the argument's dictionary keys sorted alphabetically and 
# takes the second item in the list and returns it in uppercase. The tuple 
# constructor function is used to make the key a tuple, so the output will 
# be (CHRIS,). THIS WAS WRONG. Using the tuple constructor function 
# on a string returns a tuple with each character as its elements.

# EXERCISE 2

# Use the factorial function from the math library to write some code that 
# outputs the factorial of 5. Try to write the code in three 
# different ways.

# import math

# factorial_of_5 = math.factorial(5)

# print(factorial_of_5) 

# import math as m

# factorial_of_5 = m.factorial(5)

# print(factorial_of_5)

# from math import factorial

# factorial_of_5 = factorial(5)

# print(factorial_of_5)

# EXERCISE 3 - FORGOT TO SWITCH TO MULTIPLICATION

# def product_of_squares(num1, num2):
#     return (num1**2) * (num2**2)

# print(product_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(product_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# Write a nested function in sum_of_squares that will make this 
# code work as shown.

# EXERCISE 4

# Write a function called increment_counter that increments 
# a counter variable every time it is called. You can test your
# code with the following:

# counter = 0

# def increment_counter():
#     global counter
#     counter += 1

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101

