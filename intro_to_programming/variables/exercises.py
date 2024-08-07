# Exercise 1 

# index - idiomatic 
# CatName - non-idiomatic because it is PascalCase, not snake_case 
# lazy_dog - idiomatic 
# quick_Fox - non-idiomatic because the second word is capital 
# 1stCharacter - illegal because it starts with a num 
# operand2 - idiomatic 
# BIG_NUMBER - non-idiomatic because these names are not for constants 
# pi - non-idiomatic because it is not an ASCII character 

# Exercise 2 

# same as previous 

# Exercise 3 

# index - non-idiomatic because it is not capitalized 
# CatName - non-idiomatic because it is not capitalized 
# snake_case - non-idiomatic because it is not capitalized 
# LAZY_DOG3 - idiomatic 
# 1ST - illegal starts with num 
# operand2 - non-idiomatic because it is not capitalized 
# BIG_NUMBER - idiomatic 
# pi thing - illegal because it is not an ASCII character

# Exercise 4 

# index - non-idiomatic because first letter not capitalized 
# CatName - idiomatic 
# Lazy_Dog - non-idiomatic because there is an underscore 
# 1ST - illegal because it starts with num 
# operand2 - non-idiomatic because first letter not capitalized 
# BigNumber3 - idiomatic 
# piweird i - illegal because it is not an ASCII character 

# Exercise 5 

name = "Victor" 

print(f"Good Morning, {name}")
print(f"Good Afternoon, {name}")
print(f"Good Evening, {name}") 

# Exercise 6 

age = 22 

print(f"You are {age} years old.") 
print(f"In 10 years, you will be {age + 10} years old.") 
print(f"In 20 years, you will be {age + 20} years old.") 
print(f"In 30 years, you will be {age + 30} years old.") 
print(f"In 40 years, you will be {age + 40} years old.") 

# Exercise 7 

# it will print 3 lines with victor, then 3 lines with nina 
# because name got reassigned. (it shouldn't be reassigned 
# because naming conventions imply NAME should be a constant) 

# Exercise 8 

balance = 1000.00 

balance = (balance * (1.05**5))

print(balance) 

# Exercise 9 

balance = 1000 
print(balance) 
balance *= 1.05 
print(balance) 
balance *= 1.05 
print(balance) 
balance *= 1.05 
print(balance) 
balance *= 1.05 
print(balance) 
balance *= 1.05 
print(balance) 