# Exercise 1 

# there is no index counter in the body 

# Exercise 3 

my_list = [6, 3, 0, 11, 20, 4, 17]

# counter = 0
# while counter < len(my_list): 
#     number = my_list[counter]
#     print(number) 
#     counter += 1 

# probably better to name counter index instead 
# need to initialize my_list[counter] to a variable to make more readable

# for number in my_list: 
#     print(number)
    
# don't need range(len(my_list)), can just do my_list 
# also the for loop will default to iterating through sequence?? 

# Exercise 4 (using my_list from exercise 3) 

# index = 0 
# while index < len(my_list): 
#     number = my_list[index] 
#     if number % 2 == 0: 
#         print(number) 
#     index += 1 

# for number in my_list: 
#     if number % 2 == 1: 
#         print(number) 

# Exercise 5 

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
] 

# for nested_list in my_list: 
#     for number in nested_list: 
#         if number % 2 == 0: 
#             print(number) 

# Exercise 6 

my_list = [
    1, 3, 6, 11, 
    4, 2, 4, 9, 
    17, 16, 0, 
] 

# my method 

# new_list = []
# for number in my_list: 
#     if number % 2 == 0: 
#         new_list.append("Even") 
#     else: 
#         new_list.append("Odd") 


# ternary expression 

# new_list = ['even' if number % 2 == 0 else 'odd' for number in my_list] 


# helper function version 

# def even_or_odd(number): 
#     return 'even' if number % 2 == 0 else 'odd' 
    
# new_list = [even_or_odd(number) for number in my_list]

# print(new_list)

# Exercise 7 

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# my solution
            
# def find_integers(sequence): 
#     my_list = []
#     for element in sequence: 
#         if type(element) is int: 
#             my_list.append(element) 
#     return my_list


#using comprehension 

# def find_integers(sequence): 
#     return [element for element in sequence 
#             if type(element) is int]

# integers = find_integers(my_tuple)
# print(integers) 

# Exercise 8 

my_set = {
    'Fluffy', 
    'Butterscotch', 
    'Pudding', 
    'Cheddar', 
    'Cocoa', 
} 

# new_set = { name: len(name) 
#             for name in my_set 
#             # length is odd 
#             if len(name) % 2 == 1} 

# print(new_set) 

# Exercise 9 

# for 

# def factorial(integer): 
#     result = 1 
#     for number in range(1, integer + 1): 
#         result *= number
#     return result 

# while 

# DID NOT NEED INDEX 

# def factorial(integer): 
#     result = 1 
#     while integer > 0: 
#         result *= integer 
#         integer -= 1
#     return result
    
# print(factorial(4)) 

# Exercise 10 

import random

highest = 10
# number = random.randrange(highest + 1)
# print(number)


# technically got this correct, but by setting name to an initial value instead 
# of doing do/while loop with 'while True'

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest: 
#         break 

# Exercise 11 

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
] 

# outer_index = 0 
# while outer_index < len(my_list): 
#     inner_index = 0
#     while inner_index < len(my_list[outer_index]): 
#         number = my_list[outer_index][inner_index]
#         if number % 2 == 0: 
#             print(number) 
            
#         inner_index += 1 
        
#     outer_index += 1 


# coded along vvvv

# iterate over my_list 
    # iterate over the nested list 
    
# outer_index = 0 
# while outer_index < len(my_list): 
#     inner_list = my_list[outer_index]
#     inner_index = 0 
#     while inner_index < len(inner_list): 
#         number = inner_list[inner_index] 
#         if number % 2 == 0: 
#             print(number)
#         inner_index += 1
    
#     outer_index += 1