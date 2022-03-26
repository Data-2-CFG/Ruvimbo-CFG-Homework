# coding=utf-8
# TASK 1 (Conditional flow)
#
# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.

raining = input('Is it raining? y/n ')

if (raining == 'y'):
    print("Take an umbrella")
elif (raining == 'n'):
    print("You don't need an umbrella")
#
#
# # Question 2

my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
#
# It was missing the float() function before the input, there was whitespace between boat and cost
# instead of '_', the comparison operator was incorrect and the end parenthesis on the last print statement was missing

# Question 3
# Your friend works for an antique bookshop that sells books between
# 1800 and 1950 and wants to quickly categorise books by the century and
# decade that they were written. Write a program that takes a year (e.g. 1872)
# and outputs the century and decade (e.g. "Eighteenth Century, Seventies")

year = int(input("Which year is the book from? "))

if 1800 <= year <= 1809:
    print("Nineteenth Century, Hundreds")

elif 1810 <= year <= 1819:
    print("Nineteenth Century, Tens")

elif 1820 <= year <= 1829:
    print("Nineteenth Century, Twenties")

elif 1830 <= year <= 1839:
    print("Nineteenth Century, Thirties")

elif 1840 <= year <= 1849:
    print("Nineteenth Century, Fourties")

elif 1850 <= year <= 1859:
    print("Nineteenth Century, Seventies")

elif 1860 <= year <= 1869:
    print("Nineteenth Century, Sixties")

elif 1870 <= year <= 1879:
    print("Nineteenth Century, Seventies")

elif 1880 <= year <= 1889:
    print("Nineteenth Century, Eighties")

elif 1890 <= year <= 1899:
    print("Nineteenth Century, Nineties")

elif 1900 <= year <= 1909:
    print("Twentieth Century, Hundreds")

elif 1910 <= year <= 1919:
    print("Twentieth Century, Tens")

elif 1920 <= year <= 1929:
    print("Twentieth Century, Twenties")

elif 1930 <= year <= 1939:
    print("Twentieth Century, Thirties")

elif 1940 <= year <= 1949:
    print("Twentieth Century, Fourties")

elif year == 1950:
    print("Twentieth Century, Fifties")

else:
    print("Not between 1800 and 1950!")




# TASK 2 (Lists and Dictionaries)

# Question 1
# I have a list of things I need to buy from my supermarket of choice.

shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
# print(shopping_list[:1]) #This returns the items from the beginning.
#
# #Indexes start at '0' so the program was outputting the second value.



# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to
# 'check the prices of different chocolates that I sell. I've started the program
# and included the chocolates and their prices. Finish the program by asking the user to
# input an item and then output its price.

chocolate = input("Type of chocolate ")

chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}

if chocolate == 'white':
	print(chocolates['white'])

elif chocolate == 'milk':
	print(chocolates['milk'])

elif chocolate == 'dark':
	print(chocolates['dark'])

elif chocolate == 'vegan':
	print(chocolates['vegan'])

else:

	print("Chocolate type not available")


# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers
# that represent a lottery ticket. It should then generate seven random numbers. After comparing
# the two sets of numbers, the program should output a prize based on the number of matches:
#
# £20 for three matching numbers
# £40 for four matching numbers
# £100 for five matching numbers
# £10000 for six matching numbers
# £1000000 for seven matching numbers

import random

lottery_ticket = [6, 10, 16, 31, 32, 39, 45]
print("My Lottery ticket: {}" .format(lottery_ticket))

winning_number = random.sample(range(1, 49), 7)
print("Winning numbers: {}".format(winning_number))

matches = sum(w in lottery_ticket for w in winning_number)

print("{} numbers match.".format(matches))

if matches == 3:
	print("You have won £20!")

elif matches == 4:
	print("You have won £40!")

elif matches == 5:
	print("You have won £100!")

elif matches == 6:
	print("You have won £10,000!")

elif matches == 7:
	print("You have won £1,000,000!!!")

else:
	print("You have no not won this time.")



# TASK 3 (Read and Write files)
#
# Question 1
# You're having coffee/tea/beverage of your choice with a friend that is
# learning to program in Python. They're curious about why they would use pip.
# Explain what pip is and one benefit of using pip.

# PIP is a package manager for Python which allows the user to install and manage additional Python libraries
# that are not part of the standard Python library. An advantage of PIP is that it allows the user to easily install
# software packages through the command line.


# Question 2
# This program should save my data to a file, but it doesn't work when I run it.
# What is the problem and how do I fix it?

# The string variable 'poem' should be in parentheses and
# the method was read 'r' instead of write 'w'. Solution below.

poem = ('I like Python and I am not very good at poems')
with open('poem.txt', 'w') as poem_file:
	poem_file.write(poem)
	poem_file.close()


# Question 3

# 1.Write the lyrics to a new file called song.txt

# 2. Check that a file has been created successfully.

file = open('./song.txt','r')
reading = file.read()
print(reading)


# 3. The read lines from this file and print out ONLY those lines that have a word ‘still’ in them.

file = open('./song.txt','r')
reading = file.read()
for file in reading.splitlines():
    if "still" in file:
            print(file)



#TASK 4 (API)
#
# Question 1
# In this session you used the Pokémon API to retrieve a single Pokémon.
# I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
# Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve
# the data for each Pokémon. Save their names and moves into a file called 'pokemon.txt'

import requests
from pprint import pprint as pp

url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
print(response)

pokemon = response.json()

results = (pokemon['results'])

for pokemon_name in results:
    users = pokemon_name['name']

def get_pokemon_names():
    results = (pokemon['results'])
for pokemon_name in results:
    users = pokemon_name['name']
    print(users)

with open('pokemon.txt', 'w') as text_file:
    for pokemon in users:
        text_file.writelines(users + '\n')
        text_file.close()

# Question
# 2(optional)
#
# Here is a link to a really cool API: https: // opentdb.com /
# Answer the following questions:

# What is the name of this API?
# Trivia API

# What does it do?
# It allows the programmers to generate trivia questions of different categories, types and difficulty level

# Example URL to make a call to this API?

import requests
from pprint import pprint as pp

trivia_database = 'https://opentdb.com/api.php?amount=10'

response = requests.get(trivia_database)

trivia = response.json()
pp(trivia)










