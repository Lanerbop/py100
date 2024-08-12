# Exercise 1 

# False 
# True 
# 3 
# 3 
# False 
# True 
# False 
# False 
# False  
# True 

# Exercise 2 

def even_or_odd(number): 
    if number % 2 == 0: 
        print('even') 
    else: 
        print('odd')
        
# Exercise 3 

# prints product2 then product not found.

# Exercise 5 

# prints empty because [] is a falsy value 

# Exercise 6 

def caps_if_more_than_10(string): 
    if len(string) > 10: 
        return string.upper()
    else: 
        return string
        
# print(caps_if_more_than_10('hello world')) 
# print(caps_if_more_than_10('goodbye')) 

# Exercise 7 

def value_length_category(integer): 
    if integer >= 0 and integer <= 50: 
        print(f"{integer} is between 0 and 50") 
    elif integer >= 51 and integer <= 100: 
        print(f"{integer} is between 51 and 100") 
    elif integer > 100: 
        print(f"{integer} is greater than 100") 
    else: 
        print(f"{integer} is less than 0") 

value_length_category(0) 
value_length_category(25) 
value_length_category(50) 
value_length_category(75) 
value_length_category(100) 
value_length_category(101) 
value_length_category(-1) 