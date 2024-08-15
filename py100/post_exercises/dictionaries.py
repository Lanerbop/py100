# FIRST CAR - could be improved

# car = {
#     'type': 'sedan',
#     'color': 'blue',
#     'mileage': 80_000,
# }

# print(car)

# should have used underscore for numbers and trailing comma

# ADDING THE YEAR - EASY MONEY

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year'] = 2003

# print(car)

# BROKEN ODOMETER - had to reference docs

# del car['mileage']

# print(car)

# WHAT COLOR - ez

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

# print(car['color'])

# WHAT'S MY LENGTH - ez

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

# print(len(car))

# CHECKING KEY EXERCISE

student = {
    'id': 123,
    'grade': 'B',
}

# print('name' in student)
# print('grade' in student)

# MULTIPLE CARS - WRONG

vehicles = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': '2003',
    },
    
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': '1998',
    },
    
    
}

# struggled a bit with syntax

# WHICH COLLECTION? - WRONG FORMATTING

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

# DIVIDED BY 2 - correct, but better method available

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    25,
# }

# half_numbers = []

# for value in numbers.values():
#     half_numbers.append(value // 2)
    
# print(half_numbers)

# LABELED NUMBERS - could be more efficient

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f"A {key} number is {value}.")