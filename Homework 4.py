# coding=utf-8
# TASK 2 (Exception Handling)
#
# Question 1
# Simple ATM program
#
import unittest

pin = {9217}

tries = 1

current_balance = 100

while True:
    try:
        pin_num = int(input("Welcome, please enter your pin: "))
        if not pin_num in pin:
            raise ValueError("Incorrect PIN")
        print("Pin accepted")
        print("Your account balance is: £{}\n".format(current_balance))
        break

    except ValueError:
        print("Wrong pin. Please try again \n ")
        tries += 1
        if tries == 4:
            print("Maximum 3 attempts allowed, access denied!")
            break

def withdraw():
    if pin_num in pin:
        try:

            withdraw = int(input("Enter amount to withdraw: £"))
            new_balance = current_balance - withdraw

            if new_balance >= 0:
                print ("Current Balance: £" + str(new_balance))

            else:
                print("You have insufficient funds!")

        except ValueError:
            print("Error! Invalid input please enter a valid number.")
#            Error if user enters string value

withdraw()
exit()


# TASK 3 (Testing)
#
# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to untangle some logic into smaller
# blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.
