# SECOND ELEMENT

# def second(sequence):
#     return sequence[1]
    
# print(second(['Earth', 'Moon', 'Mars']))

# LAST ELEMENT

# SECOND TO LAST ELEMENT

# def second_to_last(sequence):
#     if len(sequence) >= 2:
#         return sequence[-2]
#     else:
#         return "Sequence not long enough"
        
# print(second_to_last(['Earth', 'Moon', 'Mars']))
    
# ADD + DELETE

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# energy.remove('fossil')

# energy.insert(0, 'geothermal')

# print(energy)

# ALPHABET

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# alphabet = tuple(alphabet)

# print(alphabet)

# FILTER

# scores = [96, 47, 113, 89, 100, 102]

# low_scores = [score for score in scores if score < 100]

# print(low_scores)

# VOCABULARY

# vocabulary = [
#     ['happy', 'cheerful', 'merry'],
#     ['tired', 'sleepy', 'fatigued'],
#     ['excited', 'eager', 'enthused']
# ]

# for emotions in vocabulary:
#     for word in emotions[:2]:
#         print(word)

# EQUALITY

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]

# print(list1 == list2)

# TYPE

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = "I leave you my Kingdom, take good care of it."

# print(isinstance(some_value1, list))
# print(isinstance(some_value2, list))

# TRAVEL

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']
                
# def contains(element, collection):
#     return collection.count(element) > 0
    
# print(contains('Prague', destinations))
# print(contains('prague', destinations))

# PASSCODE

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# new_passcode = '-'.join(passcode)

# print(new_passcode)

# CHECKING ITEMS OFF GROCERY LIST

# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# while grocery_list:
#     my_item = grocery_list.pop()
#     print(my_item)

# print(grocery_list)