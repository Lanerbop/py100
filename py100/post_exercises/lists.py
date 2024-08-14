# # FIRST ELEMENT - utilize that empty list is falsy

# def first(my_list):
#     if my_list:
#         return my_list[0]
#     else:
#         return "List is empty."

# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# print(first([])) 

# LAST ELEMENT - easy

# def last(lst):
#     if lst:
#         return lst[-1]
#     else:
#         return "The list is empty."

# print(last(['Earth', 'Moon', 'Mars']))  # mars
# print(last([]))

# ADD + DELETE

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# energy.remove('fossil')
# energy.append('geothermal')

# print(energy)

# ALPHABET

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet = list(alphabet)
# print(alphabet)

# FILTER - forgot to print length 

# scores = [96, 47, 113, 89, 100, 102]

# above_100 = [score for score in scores if score >= 100]

# print(len(above_100))

# VOCABULARY - good. no hiccups. could improve naming

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for outer_list in vocabulary:
#     for word in outer_list:
#         print(word)

# EQUALITY

# This should print true because both list 1 and list 2 are 
# the same data type and contain the exact same elements.

# TYPE - COULD BE IMPROVED

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

# def is_list(variable):
#     return True if type(variable) == list else False
        
# print(is_list(some_value1))
# print(is_list(some_value2))

# print(isinstance(some_value1, list))
# print(isinstance(some_value2, list))

# TRAVEL - improvements/different method possible

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# def contains(item, lst):
#     return lst.count(item) > 0

# def contains(element, lst):
#     for item in lst:
#         if item == element:
#             return True
#     return False
        
    
# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# PASSCODE - INEFFICIENT

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

    
# print("-".join(passcode))

# CHECKING ITEMS OFF THE GROCERY LIST - didn't print item

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# def remove_item():
#     while grocery_list:
#         removed_item = grocery_list.pop(0)
#         print(removed_item)


# remove_item()
# print(grocery_list)