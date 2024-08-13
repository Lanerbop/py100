# LENGTH - v easy

# string = "These aren't the droids you're looking for."
# print(len(string))

# ALL CAPS

# string = 'confetti floating everywhere'
# uppercase_string = string.upper()

# print(uppercase_string)

# IGNORING CASE

# name = 'Roger'
# weird_name = 'RoGeR'

# def are_equal_case_insensitive(string1, string2):
#     if string1.casefold() == string2.casefold():
#         print("true")
#     else:
#         print("false")

# are_equal_case_insensitive(name, weird_name)
# are_equal_case_insensitive(name, 'DAVE')

# MULTILINE STRING - forgot newline character

# rhyme = ("A pirate I was meant to be!\n"
#          "Trim the sails and roam the sea!")

# print(rhyme)

# CONTAINS CHARACTER - could have used in keyword

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# print('x' in char_sequence)

# IS EMPTY - too verbose

# def is_empty(string):
#     return not string
    
# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

# IS EMPTY OR BLANK - fine

# def is_empty_or_blank(string):
#     return not string.strip()
    
# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# CAPITALIZE WORDS

# string = 'launch school tech & talk'
# title_string = string.title()

# print(title_string) - forgot abouts startswith method

# CHECK PREFIX

# def starts_with(string, prefix):
#     prefix_length = len(prefix)
#     return string[:prefix_length] == prefix
    
# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# COUNT SUBSTRINGS

# def count_substrings(string, substring):
#     return string.count(substring)
    
# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0