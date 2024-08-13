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

