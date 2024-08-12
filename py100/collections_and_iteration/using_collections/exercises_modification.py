# Exercise 1 - struggled to find simple answer 
# Write code to print the 5th number of range(0, 30, 2) 

# my_range = range(0, 30, 2) 

# print(my_range[4]) 

# Exercise 2 
# use slicing to write python code to print a 3 character substring of 
# 'The Launch School' that begins with the first h 

# my_string = 'Super Launch School' 
# start = my_string.index('h') 

# print(my_string[start:start + 3]) 

# this method was fine. be aware of differences - index will throw an error, 
# but if I used the find method, it would just return -1 instead 

# Exercise 3 - struggled without using linked list 
# write code to create a new tuple from (5, 6, 7, 8, 9, 10, 11) The new tuple 
# should be reverse order and exclude first and last members of original. 

# my_tuple = (5, 6, 7, 8, 9, 10, 11) 

# reversed_tuple = my_tuple[-2:0:-1]

# print(reversed_tuple) 

# Exercise 4 

# pets = {
#     'Cat':  'Meow',
#     'Cow':  'Moo',
#     'Bird': 'Tweet', 
#     'Snake': 'Hiss', 
# } 

# print(pets['Snake']) 
# print(pets.get('Kangaroo')) 
# print(pets.get('Lizard', 'it is not there broski')) 

# Exercise 5 

# can't - line 3,4,6 mdt 

# Exercise 6 

# false, false, false, false, false, true, true, false, false, false, false 

# Exercise 7 - struggled with join syntax. 
# replace all & with $

# info = 'xyz:*:4&2:42:Lee &Kim:/home/&xyz:/bin&/zsh' 

# split_info = info.split('&') 
# new_info = '$'.join(split_info) 

# print(new_info) 

# print(info.replace('&', '$')) 

# Exercise 9 
# replace 8 in third list with bird

# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12],
# ] 

# stuff[2][1] = 'bird' 

# print(stuff) 

# Exercise 10 

# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             },
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             },
#         },
#     },
# } 

# print(cats['Pete']['Cheddar']['enjoys']) 

# Exercise 11 

# false
# true 
# true 
# false 
# true 
# false 
# false - got this wrong 
# true 
# false 
# true 

# Exercise 12 - if just doing true or false, do not need function 

# def list_contains_5(my_list): 
#     if 5 in my_list: 
#         print('This list has a 5') 
#     else: 
#         print('This list does NOT have a 5') 
        
# numbers1 = [1, 3, 5, 7, 9, 11]
# numbers2 = []
# numbers3 = [2, 4, 6, 8]
# numbers4 = ['1', '3', '5']
# numbers5 = ['1', 3.0, '5'] 

# list_contains_5(numbers1)
# list_contains_5(numbers2)
# list_contains_5(numbers3)
# list_contains_5(numbers4)
# list_contains_5(numbers5) 

# print(5 in numbers1)
# print(5 in numbers2)
# print(5 in numbers3)
# print(5 in numbers4)
# print(5 in numbers5) 

# Exercise 14 - forgot to convert to list to print, otherwise easy 

# my_str = 'abc'
# my_list = ['Alpha', 'Bravo', 'Charlie']
# my_tuple = (None, True, False)
# my_range = range(10, 60, 10) 

# list_of_tuples = zip(my_str, my_list, my_tuple, my_range) 

# print(list(list_of_tuples)) 

