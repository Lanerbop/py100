# Exercise 1 

# there is no index counter in the body 

# Exercise 3 

my_list = [6, 3, 0, 11, 20, 4, 17]

# counter = 0
# while counter < len(my_list): 
#     number = my_list[counter]
#     print(number) 
#     counter += 1 

# probably better to name counter index instead 
# need to initialize my_list[counter] to a variable to make more readable

# for number in my_list: 
#     print(number)
    
# don't need range(len(my_list)), can just do my_list 
# also the for loop will default to iterating through sequence?? 

# Exercise 4 (using my_list from exercise 3) 

index = 0 
while index < len(my_list) and index % 2 == 0: 
    number = my_list[index] 
    print(number) 
    index += 1