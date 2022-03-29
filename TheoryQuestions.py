#2. Python string methods:
# describe each method and provide an example


# In Python, the capitalize() method converts first character of a string to uppercase letter and
# lowercases all other characters, if any
# string = "tommy used to WORK on the Docks."
# print(string.capitalize())



# Casefold() converts all the characters of a string to lowercase
# string = "TOMMY USED TO WORK ON THE DOCKS."
# print(string.casefold())



# center()
# string = "Sweet home alabama"
# centred_string = string.center(50)
# print(centred_string)




# count()
# string = "Singing sweet home alabama all summer long"
# count = (string.count('a'))
# print(count)



# endswith()
# string = "Singing sweet home alabama all summer long."
# string_end = (string.endswith('all summer long.',14,43))
# print(string_end)
#
# string = "Singing sweet home alabama all summer long."
# string_end = (string.endswith('all summer long',14,43))
# print(string_end)




#find()
# string = "Singing sweet home alabama all summer long."
# print(string.find('sweet'))



#format()
# print("My name is {} and I live in {}. ".format("Fiona", "Manchester"))



# index()
# string = "Singing sweet home alabama all summer long."
# print(string.index('sweet'))



# isalnum()
# string = "S1ng1n g."
# print(string.isalnum())
# Returns false
#
# string = "S1ng1ng"
# print(string.isalnum())
# Returns true




# isalpha()
# string = "Singing"
# print(string.isalpha())
# Returns true

# string = "S1ng1ng"
# print(string.isalpha())
# Returns false



# isdigit()
# string = "123456"
# print(string.isdigit())
# Returns true

# string = "1234S6"
# print(string.isdigit())
# Returns false



# islower()
# string = "i like baking"
# print(string.islower())
# Returns true

# string = "I LIKE baking"
# print(string.islower())
# Returns false


# isnumeric()
# string = "123456"
# print(string.isnumeric())
# Returns true

# string = "I LIKE baking"
# print(string.isnumeric())
# Returns false



# isspace()
# istitle()
# isupper()
# join()
# lower()
# lstrip()
# replace()
# rsplit()
# rstrip()
# split()
# splitlines()
# startswith()
# strip()
# swapcase()
# title()
# upper()