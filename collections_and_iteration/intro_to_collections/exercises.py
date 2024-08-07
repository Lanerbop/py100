# Exercise 1 

# len(people) 

# Exercise 2 

stuff = ('hello', 'world', 'bye', 'now') 

stuff = list(stuff) 

stuff[2] = 'goodbye' 

stuff = tuple(stuff)

print(stuff[2])

# Exercise 3 

# differences - lists are mutable, tuples aren't. lists have brackets, 
# tuples have parenthesis

# similarities - both are sequences. both can contain any object and don't 
# have to be the same type 

# Exercises 4 

# strings are ordered and you can access characters by indexing 

# Exercise 5 

# sets are unordered and unique. they don't support indexing bc 
# they are unordered. 

# Exercise 6 

pi = 3.141592 

str_pi = str(pi) 

# Exercise 7 

# 0 - 6 
# # 1 - 5 
# 3, 7 ,11  
# none 
# 8, 7, 6, 5, 4 

# Exercise 8 

print(list(range(3, 17, 4))) 

# Exercise 9 

# 1 - yes 
# 2 - no 
# 3 - yes 
# 4 - yes bc constructors are shallow copies 

# Exercise 10 

# it won't because sets are unordered 

# Exercise 11 

locations_of_people = {
    'Alice': 'USA', 
    'Francois': 'Canada', 
    'Inti': 'Peru', 
    'Monika': 'Germany', 
    'Sanyu': 'Uganda', 
    'Yoshitake': 'Japan', 
} 

print(locations_of_people['Monika'])