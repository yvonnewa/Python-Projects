######## 
# myinvestor1.py 
# Assignment #1 
# CMPT 120 
# Author: Yvonne Wang 
# September 21, 2019
# 
# The purpose of this investor bot is to calculate the investment return values based on user inputs.

# greeting the user 

print("Hello there!") 

# ask for the name 
name = input("What is your name? ---> ") 
print()

# answer with the name in a message 

print("Nice to meet you, " + name + "!") 

# ask for age 

age = int(input("How old are you? ---> "))
print()

# introduction to investment topic

print("Great! I want to introduce you to the world of investing.")
print()

print("If you decide that you want in, I will give you the password to enter my website.") 
print()

print("It is incredibly secure and reliable.")
print()

# rules of investment function

def investmentRules():
    print("If you invest for 5 years or fewer, you will get a percentage equal to 1/2 the number of years.")
    print()
    print("If you invest for 5 or more years, you will get 2% plus the percentage of 1/2 the number of years.")
    print()
    print("If you invest for 10 years or more, you will get an extra percentage, which is a random number that includes and is between 0 and 2.")
    print()
    return

# ask if user is interested

yesorno = input("Do you want to learn more? (Y/N) ---> ")
print()

if yesorno == "Y":
    print("Great! I'll tell you the rules then.")
    print()
    investmentRules()

elif yesorno == "N":
    print("Okay, then! Have a good day!")
    exit()

# initial capital

initial = int(input("What is your initial capital? ---> "))
print()

# years of investment

years = int(input("How many years will you be investing? ---> "))
print()

# calculate percentages

percentage1 = years//2

percentage2 = (2) + (years//2) 

import random 

minValue = 0
maxValue = 2
rannum = random.randint(0,2)

percentage3 = rannum + percentage2

if years<5:
  print("Your percentage will be " + str(percentage1)  + "%.")

elif 5<=years<10:
  print("Your percentage will be " + str(percentage2) + "%.")
  print("**TRACE, percentage is 2 +", years * 0.5)

if years>=10:
  print("Your percentage will be " + str(percentage3) + "%.")
  print("**TRACE, percentage is 2 +", years * 0.5, "+", rannum)

# ask if the user wants to invest

print()
askInvest = input("Do you want to invest with me? (Y/N) ---> ")
print()

if askInvest == "Y":
    print("Great! I'll give you the password then.")

elif askInvest == "N":
    print("Okay, then! Have a good day!")
    exit()

# password creator

n = age % 7

passwordstart = name[0] * n

passwordend = name[-1]

passwordlength = len(passwordstart + passwordend)

if (passwordlength % 2) == 0:
  exclamation = str("!")

else:
  exclamation = str("!!")

# password statement

print("Your password is... ", passwordstart + passwordend + exclamation)



















