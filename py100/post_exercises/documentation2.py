# STRING FORMATTING 

name = 'Victor' 
profession = 'programmer' 

# string = 'Hello {}. You are a {}'.format(name, profession) 
# did not need numbers inside brackets 

# string = f"Hello {name}. You are a {profession}."

# print(string) 

# STYLE GUIDE - One personal note: stop
# using trailing whitespace, limit comments to 72 characters, 
# use complete sentences, and limit code to 79 characters. 
# ON THIS EXCERCISE, I FORGOT TO SWITCH PASCALCASE TO 
# SNAKE CASE.

# ice_cream_density = 10

# while ice_cream_densit > 0:
#     print('Drip...')
#     ice_cream_densit -= 1

# print('The ice cream melted.')

# ARITHMETIC OPERATOR PRECEDENCE

# 4 * 5 + 3**2 / 10

# The corresponding section is under "Operator Precedence". It 
# generally follows PEMDAS. This means the result should be: 
# Exponent - 4 * 5 + 9 / 10 
# M/D left to right - 20 + 0.9 
# A/S left to right - 20.9

# It is a good idea to use parenthesis because some coworkers may 
# not know PEMDAS too well.

# DATE - I used the today function instead of the now function, but
# now is better because it has a tz/timezone parameter. However, 
# I could not figure out how to return the current timezone.

# import datetime

# print(datetime.datetime.today())
# print(datetime.datetime.now())

# WHICH YEAR IS THIS?

# from datetime import date

# today = date.today()

# today_year = today.year
# iso_year = today.isocalendar()[0]

# print(today_year, iso_year, today.isocalendar())

# The year attribute returns just the year, while the isocalendar 
# method returns a tuple with named year, week, and weekday.
# MISSED - ISO year may differ on start and end of year due to 
# how iso and gregorian calculate the year differently.

# ARGUMENT SIGNATURES

# The str.join method expects 1 argument, which is the character the 
# strings will be joined on. If called with fewer or more arguments, 
# the result would be a type error.

# FIND SUBSTRING

# To find out if a string contains a specific substring, use the in 
# operator to test for membership. The syntax to print 'True' if 
# a string contains a specific substring is: 
# print("substring" in "string")

# print("hell" in "hello")

# SYNTAX ERROR

# speed_limit = 60
# current_speed = 80

# if current_speed > speed_limit:
#     print('"People are so bad at driving cars that '
#           "computers don\'t have to be that good to be "
#           'much better." -- Marc Andreessen')
          
# There was a missing semicolon after the conditional.

# TYPE ERROR

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5