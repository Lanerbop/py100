# FIRST CAR

# car = {
#     'type': 'sedan',
#     'color': 'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2001

# del car['mileage']

# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print('name' in student)
# print('grade' in student)

# MULTIPLE CARS

# vehicles = {
#     'car': {
#         'type': 'sedan',
#         'color': 'blue',
#         'year': 2003,
#     },
    
#     'truck': {
#         'type': 'pickup',
#         'color': 'red',
#         'year': 1998,
#     },
    
# }

# WHICH COLLECTION?

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# car = (
#     ('type', 'sedan'),
#     ('color', 'blue'),
#     ('year', '2003')
# )

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

# def twice_numbers(collection):
#   return [number * 2 for number in numbers.values()]
# print(twice_numbers(numbers))

# LABELED NUMBERS

# for key, value in numbers.items():
#     print(f"A {key} number is {value}.")