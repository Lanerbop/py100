# PART 1 - WRONG

# 20 will be printed

# PART 2 - correct. easy

# There will be an error because my_function tries to 
# reinitialize variable x, but it has never been 
# initialized in the current scope.

# PART 3 - correct. easy

# 1 will be printed because a is initialized to 1 in the 
# local scope of my_function

# PART 4

# 1 will be printed because my_function can access a. 
# It just can't reassign it.

# PART 5

# an error will be thrown because a is initialized after 
# it is called in the local scope.

# PART 6

# 1 will be printed because a is assigned to the value 1 
# it the global scope. local reassignment does not affect 
# the a in the global scope

# PART 7

# 2 will be printed because a is reassigned to 2 in the 
# global scope whenever my_function is called.

# PART 8

# an error will be thrown because greeting is called before 
# it is initialized.

# PART 9 - WRONG

# 7 will be printed because my_function creates b = 17 in 
# the local scope. The print function call is in the global 
# scope.

# PART 10 - correct. 

