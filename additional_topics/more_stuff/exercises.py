# Exercise 1 - wrong, only the index is provided, not entire dictionary 

# the function sorts (non-mutating) a dictionary's keys ascending, and then 
# takes the second key and capitalizes it fully. The output should be: 
# CHRIS 

# Exercise 2 

# import math 

# sqrt_37 = math.sqrt(37) 

# import math as m 

# sqrt_37 = m.sqrt(37) 

# from math import sqrt

# print(sqrt_37)
# print(sqrt(37)) 

# Exercise 3 

# def sum_of_squares(num1, num2): 
#     def square(num): 
#         return num**2
        
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12) 

# Exercise 4 - have to set counter to global before modifying it 

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

# Exercise 5 

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()