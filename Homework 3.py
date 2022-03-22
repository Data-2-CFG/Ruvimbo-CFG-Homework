
# TASK 1 (Conditional flow)
#
# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.

raining = input('Is it raining? y/n ')

if (raining == 'y'):
    print("Take an umbrella")
elif (raining == 'n'):
    print("You don't need an umbrella")



# Question 2

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money < boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# It was missing the int function before the input and the end parenthesis on the last print statement
