# coding=utf-8
# Question 1
# Complete definitions for key Git & GitHub terminology
# GIT WORKFLOW FUNDAMENTALS


# Working Directory
# Staging Area
# Local Repo (head)
# Remote repo (master)


# WORKING DIRECTORY STATES:
# Staged
# Modified
# Committed


# GIT COMMANDS:
# Git add
# Git commit
# Git push
# Git fetch
# Git merge
# Git pull


# TASK 2 (Exception Handling)
#
# Question 1
# Simple ATM program
#

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

        except NameError:
            print("Error! Invalid input please enter a valid number.")
#            Error if user enters string value

withdraw()












# 4.Now we need to simulate cash withdrawal
# 5.Accept the withdrawal amount
# 6.Subtract the amount from the account balance and display the remaining balance
# (NOTE! The balance cannot be negative!)
# 7.However, when a user asks to withdraw more money than they have on their account
# then you need to raise an error an exit the program.


# TASK 3 (Testing)
#
# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to untangle some logic into smaller
# blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.
