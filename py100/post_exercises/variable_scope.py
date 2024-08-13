# PART 1

# The code will print 20 because True is a truthy expression. 
# Note that if statements do not create a local scope. 

# PART 2

# There will be a UnboundLocalError because x was never initialized 
# within the scope of my_function. WRONG it is an UnboundLocalError 
# instead of a name error.

# PART 3

# 1 will be printed.

# PART 4 - WRONG. It will print 1.

# 1 will be printed because a is a global variable. We just can't 
# REASSIGN or MAKE CHANGES to a global variable.

# PART 5 - WRONG

# WRONG - 1 will be printed. A local variable 'a' is assigned in my_function
# RIGHT - Python detected 'a' is initialized after it is printed, 
# and even though a is assigned globally, an unbound local error 
# still occurs

# PART 6

# 1 is printed because a = 2 is only within the local scope.

# PART 7

# 2 will be printed because a is specified to be a global variable 
# within the function definition.

# PART 8

# A NameError will occur because greeting is called before 
# its initialization.

# PART 9 - WRONG

# 7 will be printed because a is initialized as a local variable 
# inside the function.

# PART 10 - WRONG

# [10, 2, 3]