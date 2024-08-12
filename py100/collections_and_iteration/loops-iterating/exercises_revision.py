# Exercise 3 - this was v easy

my_list = [6, 3, 0, 11, 20, 4, 17] 

# index = 0 
# while index < len(my_list): 
#     number = my_list[index]
#     print(number) 
#     index += 1 

# for number in my_list: 
#     print(number) 

# Exercise 5 - this was easy

# print('These are the even values using a while loop') 
# index = 0 
# while index < len(my_list): 
#     number = my_list[index] 
#     if number % 2 == 0: 
#         print(number) 
#     index += 1 
    
# print('These are the odd values using a for loop') 
# for number in my_list: 
#     if number % 2 == 1: 
#         print(number) 

# Exercise 6 - for challenge, do this with string interpolation - needed review 
# with comprehension syntax, but otherwise easy

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
] 

# new_list = [ 'even' if number % 2 == 0 else 'odd' for number in my_list ] 

# new_list = [] 
# for integer in my_list: 
#     if integer % 2 == 0: 
#         new_list.append('even')
#     else: 
#         new_list.append('odd')

# print(new_list) 

# Exercise 7 - forgot to return in function

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_string(sequence): 
#     return [ element for element in sequence if type(element) is str ]
    
# strings = find_string(my_tuple) 
# print(strings)
    
# Exercise 8 - easy. did even instead of odd 

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# } 

# my_dict = { string: len(string) 
#             for string in my_set 
#             if len(string) % 2 == 0 } 

# print(my_dict) 

# Exercise 9 - easy 

# def factorial(integer): 
#     result = 1
#     for integer in range(integer, 0, -1): 
#         result *= integer 
#     return result 

# print(factorial(6)) 

# Exercise 10 - needed to remember syntax for do/while loop 
# it involves while True, and then breaking at a certain condition 

# import random

# highest = 10


# while True: 
#     number = random.randrange(highest + 1) 
#     print(number) 
#     if number == highest: 
#         break 

# Exercise 11 - kinda hard to mental through, but I got working code 1st try 

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
] 

# outer_index = 0 
# while outer_index < len(my_list): 
#     inner_index = 0 
#     inner_list = my_list[outer_index] 
#     while inner_index < len(inner_list): 
#         number = inner_list[inner_index] 
#         if number % 2 == 0: 
#             print(f"{number} is even")
#         inner_index += 1 
#     outer_index += 1