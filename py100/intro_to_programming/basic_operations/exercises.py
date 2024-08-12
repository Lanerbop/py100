# Exercise 1 

first_name = "Lane"
last_name = "Wofford"
full_name = f"{first_name}  {last_name}" 


print(full_name)

#Exercise 2 

number = 4936 
ones = number % 10 
tens = int((number % 100 - ones) / 10) 
hundreds = int((number % 1000 - tens * 10 - ones) / 100) 
thousands = int((number - hundreds * 100 - tens * 10 - ones) / 1000) 


print(f"{ones} {tens} {hundreds} {thousands}")

#that was a mess 

#Exercise 3 

#print("5" + "10") would result in the output "510"
#because 5 and 10 are strings. adding them would result in string
#concatenation. 

#Exercise 4 

print(int("5") + int("10"))

#Exercise 5 

#Yes, it would result in an indexing error. 

#Exercise 6 

#False 

#Exercise 7 

#raises ValueError because string does not represent a valid integer

#Exercise 8 

#This would result in true because strings are evaluated character by character 


