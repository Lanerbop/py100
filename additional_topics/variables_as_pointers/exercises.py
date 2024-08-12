# Exercise 1 

# first expression means the values are equivalent 
# second expression means both objects have the same exact identity / they 
# are the exact same object 

# Exercise 2 

# it will print {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} 
# this is because when set2 is initialized to set1, it then points at the 
# same object, so when set1 is mutated, set2 is mutated as well (bc they 
# are representing the exact same object) 

# Exercise 3 - WRONG

# it actually prints "The Life of Brian" because dict2 is not the same object
# as dict1. 

# Exercise 4 - indexing error on my part 

# it would print [1, 42, 3] because we created a shallow copy and mutated 
# a mutable data type 

# Exercise 5 

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1) # You may modify the `???` part
#             # of this line

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1]) 

# Exercise 6 

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2) # false
print(dict1['a']    is dict2['a']) # true - I got this wrong, said 'false'
print(dict1['a'][0] is dict2['a'][0]) # true
print(dict1['a'][1] is dict2['a'][1]) # true
print(dict1['b']    is dict2['b']) # true
print(dict1['b'][0] is dict2['b'][0]) # true
print(dict1['b'][1] is dict2['b'][1])# true