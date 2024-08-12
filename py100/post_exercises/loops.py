# LOOP AND PRINT - v easy

# for num in range(0, 11, 2):
#     print(num)

# COUNTDOWN - v easy

# for i in range(10, 0, -1):
#     print(i)
    
# print('Launch!')

# TRIPLE GREETING - use "_" when not using loop variable

# greeting = 'Aloha!'

# for _ in range(3): 
#     print(greeting)

# count = 1

# while count <= 3:
#     print(greeting)
#     count += 1

# TAKE TWO

# for num in range(1, 101):
#     print(num * 2)

# LOOPING OVER LIST ELEMENTS

# lst = [1, 3, 7, 15]
# index = 0

# while index < len(lst):
#     print(lst[index])
#     index += 1
    
# further explanation - there would be no output and no error. This 
# is because index == len(list), so the while loop never executes

# GREET YOUR FRIENDS - very easy

# friends = ['Sarah', 'John', 'Hannah', 'Dave']

# for friend in friends:
#     print(f"Hello, {friend}!")

# CONTINUE - used == instead of is

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]
          
# for city in cities:
#     if city is None:
#         continue
    
#     print(len(city))

# AND ON AND ON AND ON

# while True:
#     print("and on")
#     break
    
# the loop keeps running because while loops continue looping 
# while the statement is truthy, which True always is

# FINDING NEMO - pretty easy

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

# index = 0
# while index < len(fish_list):
#     fish_name = fish_list[index]
#     print(fish_name)
#     if fish_name == 'Nemo':
#         break

#     index += 1
    
# LOOP ON COMMAND - use print to provide user feedback

# while True:
#     print('Should I stop looping?')
#     answer = input()
#     if answer == 'yes':
#         break
#     print("Incorrect answer. Please input 'yes'.")

