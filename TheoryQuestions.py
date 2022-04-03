#2. Python string methods:

# capitalize()

string = "tommy used to WORK on the Docks."
print(string.capitalize())
# This converts the first character of a string to a uppercase letter and
# lowercases all other characters.


# casefold()

string = "TOMMY USED TO WORK ON THE DOCKS."
print(string.casefold())
# converts all the characters of a string to lowercase


# center()

string = "Sweet home alabama"
centred_string = string.center(50)
print(centred_string)
# center aligns the string


# count()

string = "Singing sweet home alabama all summer long"
count = (string.count('a'))
print(count)
# counts the number of occurences of a substring in a given string


# endswith()

string = "Singing sweet home alabama all summer long."
string_end = (string.endswith('all summer long.',14,43))
print(string_end)

string = "Singing sweet home alabama all summer long."
string_end = (string.endswith('all summer long',14,43))
print(string_end)
# Returns true if the string ends with s specified value


#find()

string = "Singing sweet home alabama all summer long."
print(string.find('sweet'))
# Returns the first occurence of the specified value


#format()

print("My name is {} and I live in {}. ".format("Fiona", "Manchester"))
# Formats the specified val,ue and inserts them into the strings placeholder


# index()

string = "Singing sweet home alabama all summer long."
print(string.index('sweet'))
# Returns the first occurence of the specified value


# isalnum()

string = "S1ng1n g."
print(string.isalnum())
# Returns false

string = "S1ng1ng"
print(string.isalnum())
# Returns true
# Returns true if the characters are alphanumeric and false if not


# isalpha()

string = "Singing"
print(string.isalpha())
# Returns true

string = "S1ng1ng"
print(string.isalpha())
# Returns false
# Returns true if all the characters in the string are alphabets



# isdigit()

string = "123456"
print(string.isdigit())
# Returns true

string = "1234S6"
print(string.isdigit())
# Returns false
# Returns true if all the characters in the string are numbers


# islower()

string = "i like baking"
print(string.islower())
# Returns true

string = "I LIKE baking"
print(string.islower())
# Returns false
# Returns true if all characters in the string are lower case letters


# isnumeric()

string = "123456"
print(string.isnumeric())
# Returns true

string = "I LIKE baking"
print(string.isnumeric())
# Returns false
# Returns true if all characters in the string are numeric


# isspace()

string = "  "
string = string.isspace()
print(string)
# Returns true if all the characters in the string are whitespaces and returns false if not


# istitle()

string = "Sweet Home Alabama"
text = string.istitle()
print(text)
# Returns true if all the characters in a string start with an upper case letter
#
#
# isupper()

string = "SWEET HOME ALABAMA"
text = string.isupper()
print(text)
# Returns true if all characters in the string are upper case letters
#

# join()

shop = ('steak', 'cheese', 'milk')
list = " ".join(shop)
print(list)
# Takes the elements of an iterable and converts it into a string


# lower()

string = "SWEET home ALABAMA"
text = string.lower()
print(text)
# Converts upper case letters of a string into lower case
#
#
# lstrip()

string = "         eclipse          "
text = string.lstrip()
print("total",text,"of the heart")
# Removes all the whitespace to the left of the string
#
#
# replace()

string = "Humpty dumpty sat on a wall. Humpty dumpty had a great fall"
text = string.replace("Humpty dumpty", "Jack")
print(text)
# Replaces the matching occurrence of the old word with a new one
#
#
# rsplit()

shop = "steak, cheese, milk"
list = shop.rsplit(",")
print(list)
# Splits the llist into a string
#
#
# rstrip()

string = "         eclipse          "
text = string.rstrip()
print("total",text,"of the heart")
# Removes all the whitespace to the right of the string
#
#
# split()

string = "Total eclipse of the heart"
text = string.split()
print(text)
# Splits the string into a list
#
#
# splitlines()

string = "Turn around bright eyes\n Total eclipse of the heart"
text = string.splitlines()
print(text)
# Splits the string into a list where there are line breaks
#
#
# startswith()

string = "My name is Jessica Day"
text = string.startswith("My")
print(text)
# Returns true if the string starts with the specified string and if not returns false
#
#
# strip()

string = "         Jessica Day.          "
text = string.strip()
print("My name is",text, "I am a teacher")
# Returns a string by removing the leading and trailing characters
#

# swapcase()

string = "My name is JESSICA DAY"
text = string.swapcase()
print(text)
# Swaps the cases of a string and makes lower case letters into upper case letters and vice versa
#

# title()

string = "My name is Jessica Day"
text = string.title()
print(text)
# Capitalises the first character of every word in the string
#

# upper()

string = "My name is Jessica Day"
text = string.upper()
print(text)
# Converts all words in a string to upper case letters



# 3. Pythonlistmethods:
# describe each method and provide an example

# append()

fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
fruits.append('mango')
print(fruits)
# Appends the specified element to the end of the list


# clear()

fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
fruits.clear()
print(fruits)
# Clears all the items from a list


# copy()

fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
fruits.copy()
print(fruits)
# This returns a copy of the list


# count()

fruits = ['cherry', 'grape', 'blueberry', 'grape', 'guava']
count = fruits.count('grape')
print(count)
# Returns the number of times an element appears on a list


# extend()

old_list = ['cherry', 'grape', 'blueberry', 'grape', 'guava']
new_list = ['pizza', 'pasta']
new_list.extend(old_list)
print(new_list)
# Appends the old list to the end of the new list


# index()

fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
index = fruits.index('banana')
print(index)
# Returns the index of the specified element in the list


# insert()

fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
fruits.insert(4, 'apple')
print(fruits)
# Inserts the element to the list at the specified index



# pop()

fruits = ['cherry', 'grape', 'apple', 'banana', 'guava']
fruits.pop(2)
print(fruits)
# Removes an item in the list at a given index



# remove()

fruits = ['cherry', 'grape', 'apple', 'banana', 'guava']
fruits.remove('grape')
print(fruits)
# Removes a specified item in the list


# reverse()

fruits = ['cherry', 'grape', 'apple', 'banana', 'guava']
fruits.reverse()
print(fruits)
# Reverses the elements of list


# sort()

fruits = ['cherry', 'grape', 'apple', 'banana', 'guava']
fruits.sort()
print(fruits)
# Sorts the elements of the list in alphabetical order


# 4. Python tuple methods:

# count()

list = ['a', 'b', 'c', 'c', 'd', 'e', 'c']
count = list.count('c')
print(count)
# Returns the number of times a specific values appears in a tuple


# index()
#
fruits = ['cherry', 'grape', 'blueberry', 'banana', 'guava']
index = fruits.index('banana')
print(index)
# Returns the index of the specified element in the list




# 5. Python dictionary methods:

# clear()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
employee.clear()
print(employee)
# Removes all elements from the list

# copy()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
employee.copy()
print(employee)
# Returns a copy of the dictionary


# fromkeys()

employee = {"Name", "Surname", "Job_title"}
value = "Unknown"
dictionary = dict.fromkeys(employee, value)
print(dictionary)
# Returns the dictionary with specified keys and values


# get()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
value = employee.get('Job_title')
print(value)
# Returns the value of the specified key

# items()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
value = employee.items()
print(value)
# Returns all the items of a dictionary


# keys()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
value = employee.keys()
print(value)
# Returns the keys of a dictionary


# pop()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
employee.pop("Job_title")
print(employee)
# Removes a specified item from the dictionary


# popitem()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
employee.popitem()
print(employee)
# Removes the last item to be added to the dictionary


# setdefault()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job_title": "Regional Manager"
}
value = employee.setdefault("Surname")
print(value)
# Returns the value of the key if it's in the dictionary


employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job title": "Regional Manager"
}
value = employee.setdefault("Dundie Awards", 17)
print(employee)
# Inserts the key with a value to the dictionary if it's not already in the dictionary


# update()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job title": "Regional Manager"
}
employee.update({"Dundie Awards": "17"})
print(employee)
# Inserts new key and value to the dictionary

# values()

employee = {
  "Name": "Michael",
  "Surname": "Scott",
  "Job title": "Regional Manager"
}
dict_values = employee.values()
print(dict_values)
# Returns the values of the dictionary



# 6. Python set methods:

# add()

shopping = {'milk', 'bread', 'coffee', 'butter'}
shopping.add('eggs')
print(shopping)
# Adds item to the set


# clear()

shopping = {'milk', 'bread', 'coffee', 'butter'}
shopping.clear()
print(shopping)
# Removes all elements from the set


# copy()

shopping = {'milk', 'bread', 'coffee', 'butter'}
shopping.copy()
print(shopping)
# Copies all elements of a set


# difference()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
new_items = tdy_shop.difference(yst_shop)
print(new_items)
# Returns the difference between two sets


# intersection()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
new_items = tdy_shop.intersection(yst_shop)
print(new_items)
# Returns the matching items in two sets


# issubset()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk','bread', 'coffee', 'butter'}
new_items = tdy_shop.issubset(yst_shop)
print(new_items)
# Returns true if all of the elements in the set are in the specified set


# issuperset()

tdy_shop = {'milk', 'bread', 'coffee', 'butter', 'rice', 'brocolli', 'cheese'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
new_items = tdy_shop.issuperset(yst_shop)
print(new_items)
# Returns true if all of the elements in the set are in the original set


# pop()

shop = {'milk', 'bread', 'coffee'}
shop.pop()
print(shop)
# Removes a random item from the set


# remove()

shop = {'milk', 'bread', 'coffee'}
shop.remove('bread')
print(shop)
# Removes specific element from the set


# symmetric_difference()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
new_items = tdy_shop.symmetric_difference(yst_shop)
print(new_items)
# Returns all items from both sets excluding the items which are present in both sets


# union()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
new_items = tdy_shop.union(yst_shop)
print(new_items)
# Returns all items from both sets


# update()

tdy_shop = {'milk', 'bread', 'coffee', 'butter'}
yst_shop = {'rice', 'brocolli', 'cheese', 'milk'}
tdy_shop.update(yst_shop)
print(tdy_shop)
# Inserts the items from the second set into the first set


# 7. Python file methods:

# read()

file = open('./song.txt', 'r')
print(file.read())
# Returns the entire contents of a file


#readline()
#
file = open('./song.txt', 'r')
print(file.readline())
#Returns the first line of a file


# readlines()

file = open('./song.txt', 'r')
print(file.readlines())
# Returns all the lines of a file as a list


# write()

file = open('./song.txt', 'w')
file.write("New song")
# Writes text to a new file and overwrites existing files


# writelines()

file = open('./song.txt', 'w')
file.writelines(["New song"])
# writes the items of a list to the file.