# Exercise 1 

# my_range = range(0, 25, 3) 

# print(my_range[6]) 

# Exercise 2 

# my_string = 'Launch School' 

# start = my_string.find('c')

# my_substring = my_string[start : start + 6]

# print(my_substring) 

# Exercise 3 

# starting_tuple = (1, 2, 3, 4, 5) 

# ending_tuple = starting_tuple[3:0:-1]

# print(ending_tuple) 

# Exercise 4 

# pets = {
#     'Cat': 'Meow', 
#     'Dog': 'Bark', 
#     'Bird': 'Tweet', 
# } 

# print(pets['Dog']) 
# print(pets.get('Lizard')) 
# print(pets.get('Lizard', '<silence>')) 

# Exercise 5 

# lines 3, 4, and 6 can't be used as a key because they are mutable data types 

# Exercise 6 

# false, false, false, false, false, true, true, false, false, false, false 

# Exercise 7 

#info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh' 

#info_list = list(info) 

#info_list[3] = '+' 
#info_list[5] = '+' 
#info_list[8] = '+' 
#info_list[11] = '+' 
#info_list[29] = '+' 

#info = ''.join(info_list) 

# or 

# info = info.replace(':', '+') 

# or 

#parts = info.split(':') 
#info = '+'.join(parts)

#print(info) 

# Exercise 8 

# the rfind method on line 3 is performed on a substring, and the returned index
# value is the index value in respect to the substring. The rfind method 
# used on line 4 is performed on the whole string with an index range in the 
# argument, meaning the returned value is in respect to the entire string 

# Exercise 9 

#stuff = [
#    ['hello', 'world'],
#    ['example', 'mem', None, 6, 88],
#    [4, 8, 12],
#] 

#stuff[1][3] = 606 

#print(stuff) 

# Exercise 10 

# print(cats['Pete']['Cocoa']['enjoys']) 

# Exercise 11 

# False 
# True 
# True 
# False 
# True 
# False
# False 
# True 
# False 'in' ONLY CHECKS VALUE GOT THIS WRONG
# True those are equal sets GOT THIS WRONG  

# Exercise 12 

#numbers1 = [1, 3, 5, 7, 9, 11]
#numbers2 = []
#numbers3 = [2, 4, 6, 8]
#numbers4 = ['1', '3', '5']
#numbers5 = ['1', 3.0, '5'] 

#print(3 in numbers1) 
#print(3 in numbers2)
#print(3 in numbers3)
#print(3 in numbers4)
#print(3 in numbers5)

# Exercise 13 

# True 
# False 
# True 
# False 

# Exercise 14 

#my_str = 'abc'
#my_list = ['Alpha', 'Bravo', 'Charlie']
# = (None, True, False)
#my_range = range(10, 60, 10) 

# result = list(zip(my_str, my_list, my_tuple, my_range)) 

#print(result) 

# Exercise 15 

# dict_keys(['Cat', 'Bird', 'Snake']) # KINDA WRONG. FORGOT IT STARTED 
# WITH FUNCTION DICT_KEYS