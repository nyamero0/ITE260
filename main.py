#!/usr/bin/python3

#################################
#                               #
#       PYTHON ACTIVITY #1      #
#                               #
#################################

# Author: Genesis C. Matic
# Section: BSIT1 - 02


# 1. [START]

iLove = "I love"
subject = "Python 3.8!"
print(iLove + " " + subject)

# 1. [END]

# =~=~=~=~=~=~=~=~=~=~= #

# 2. [START]

price = 42.99
weight = 30

print("Price: $" + str(price))
print("Weight: " + str(weight) + " lbs.")

# 2. [END]

# =~=~=~=~=~=~=~=~=~=~= #

# 3. [START]

capital = 1000
rate = 0.03
years = 5

value = capital * (1 + rate) ** years
print("The future value of the investment: " + str(round(value, ndigits=2)) + " USD")

# 3. [END]

# =~=~=~=~=~=~=~=~=~=~= #

# 4. [START]

userName = input("What is your name: ")
print("Hello, Sir " + userName)

# 4. [END]

# =~=~=~=~=~=~=~=~=~=~= #

# 5. [START]

firstSeason = input("Enter the First Season: ")
secondSeason = input("Enter the Second Season: ")
thirdSeason = input("Enter the Third Season: ")
fourthSeason = input("Enter the Fourth Season: ")
print(
    "You Have ENTERED the following season and those are " + firstSeason + ", " + secondSeason + ", " + thirdSeason + " and " + fourthSeason
    )

# 5. [END]