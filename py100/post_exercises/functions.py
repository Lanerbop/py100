# FUNCTION - forgot print

# def multiply(num1, num2):
#     return num1 * num2
    
# print(multiply(12, 4))

# PRINT QUOTE

# def bruce_eckel_quote():
#     print("Python is executable pseudocode.")
    
# bruce_eckel_quote()

# this returns None

# CITE THE AUTHOR - I forgot to add quotes. 

# def cite(author, quote):
#     print(f"{author} said: \"{quote}\"")
    
# cite('Bruce Eckel', 'Python is executable pseudocode.')

# SQUARED NUMBER

# def square_number(num):
#     return num**2
    
# print(square_number(3))

# DISPLAY DIVISION

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()

# There was no function call. If there was a proper function call, 
# the output would be 3 / 1 = 3 \n 6 / 2 = 3..

# THREE-WAY COMPARISON

# def compare_by_length(string1, string2):
#     if len(string1) < len(string2):
#         return -1
#     elif len(string1) > len(string2):
#         return 1
#     else: # lengths are equal
#         return 0
        
# print(compare_by_length('patience', 'perseverance')) # -1
# print(compare_by_length('strength', 'dignity'))      #  1
# print(compare_by_length('humor', 'grace'))

# TRANSFORMATION - I forgot to assign string.replace to a new string. 
# Strings are immutable!!!! Next time, try without replace method!

# string = 'Captain Ruby'
# new_string = string.replace('Ruby', 'Python')

# print(new_string)

# INTERNATIONALIZATION 1

def greet(language_code):
    if language_code == 'en':
        return "Hi!"
    elif language_code == 'fr':
        return "Salut!"
    elif language_code == 'pt':
        return "Olá!"
    elif language_code == 'de':
        return "Hallo!"
    elif language_code == 'sv':
        return "Hej!"
    elif language_code == 'af':
        return "Haai!"
    else:
        return ("Sorry, that is not a language code that is " 
                "currently supported.")
        

# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!
# print(greet("yoooooo"))

# LOCALE PART 1 - I assumed they would always be two characters at 
# the start of the string. It is probably better to use a different 
# method.

# def extract_language(locale):
#     return locale[:2]
    
def extract_language(locale):
    return locale.split('_')[0]
    
# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko

# LOCALE PART 2

def extract_region(locale):
    locale_no_lang = locale.split("_")[1] # remove language code
    region_code = locale_no_lang.split(".")[0] # isolate region code
    return region_code
    
# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

# INTERNATIONALIZATION 2

def local_greet(locale):
   region = extract_region(locale)
   language = extract_language(locale)
   if region == 'US':
       return "Hey!"
   elif region == 'GB':
        return 'Hello!'
   elif region == 'AU':
       return 'Howdy!'
   else:
       return greet(language)
   
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
