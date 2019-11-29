#######
# myfoodbot2.py
# author: Yvonne Wang
# date: 10/07/2019
#
# The purpose of this program is to allow the user to order items off of a menu.

# This is the provided code

initLists = input("Execute with new lists (n) or original lists (o)? ==> ")
print()

if initLists == "n":

    print("\nTo start please input the lists exactly using the list format")
    print("Lists should have at least 1 dish and not more than 10 dishes")
    print("Lists with prices correspond exactly to lists with dishes\n")

    vietnamese_dishes = eval(input("List of Vietnamese dishes ==> "))
    vietnamese_dish_prices = eval(input("List of Vietnamese dishes prices ==> "))
    print()
    italian_dishes = eval(input("List of Italian dishes ==> "))
    italian_dish_prices = eval(input("List of Italian dishes prices ==> "))

else:

    print("Now lists are initialized in the program ")

    vietnamese_dishes = ["Pho", "Fried rice", "Pancake", "Steamed sticky rice"]
    vietnamese_dish_prices = [7.50, 6.75, 5.15, 8.25]

    italian_dishes = ["Pizza", "Meatball spaghetti", "Pasta"]
    italian_dish_prices = [7.15, 6.25, 5.00]


# TRACE PRINTING IN ANY CASE

print ("\n*** TRACE Vietnamese ", vietnamese_dishes, vietnamese_dish_prices)
print ("\n*** TRACE Italian ", italian_dishes, italian_dish_prices)

# Introduction to the foodbot

print()
print("Hi, welcome to the foodbot!")
print()

# Asking user for their Name

def namefunction():
  name = input("What is your name? ==> ")
  print()
  print("Hello,", name, ", we offer Vietnamese and Italian style food. You may choose two dishes to order.")
  print()
  print("If you are not sure what to order, we can choose a popular dish for you!")
  print()
  return

namefunction()

# Allowing the user to order their first dish

order1 = input("What would you like to order? ==> ")
print()

# This is the cost variable

accum = 0

# User's first order - either choosing a Vietnamese dish, Italian dish, or receiving a random dishes

# The cost, accum, will begin to accumulate

# If the user chooses a Vietnamese dish:

if order1 in vietnamese_dishes:
  pos = vietnamese_dishes.index(order1)
  print("It appears you like Vietnamese food.")
  print()
  print("***TRACE: dish", order1, "costs", vietnamese_dish_prices[pos])
  print() 
  accum = accum + vietnamese_dish_prices[pos]

# If the user chooses an Italian dish:

elif order1 in italian_dishes:
  pos = italian_dishes.index(order1)
  print("It appears you like Italian food.")
  print()
  print("***TRACE: dish", order1, "costs", italian_dish_prices[pos])
  print() 
  accum = accum + italian_dish_prices[pos]

# If the user chooses a dish that is not on the menu, a random dish will be decided on for them

else:
  print("Okay, we will choose a dish for you.")
  import random
  randomdish = vietnamese_dishes + italian_dishes
  allprices = vietnamese_dish_prices + italian_dish_prices
  randish1 = (random.choice(randomdish))
  pos = randomdish.index(randish1)
  print("Your random dish is", randish1 + ".")
  print()
  print("***TRACE: dish", randish1, "costs", allprices[pos])
  print() 
  accum = accum + allprices[pos]

  # The user has the option to make their chosen dish a suggestion for a future menu

  futuredish = input("Also, would you like to suggest this as a future dish idea? (Y/N) ==> ")
  print()
  if futuredish == "Y":
    print("Thanks for your suggestion.")
    print()
  if futuredish == "N":
    print("Thanks anyway!")
    print()

# Second order

yesorno = input("Do you want to order another dish? (Y/N) ==> ")
print()

# The menu code for the second order

viet2 = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"]

ital2 = ["i1", "i2", "i3", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10"]

# The formatting of the lists for the menu codes and the dishes

def menufunction():
  print("All our available dishes are:")
  print()
  print("===========================================")
  print()

  for i in range(len(vietnamese_dishes)):
    print(viet2[i] + '\t ' + vietnamese_dishes[i])
  print()

  for i in range(len(italian_dishes)):
    print(ital2[i] + '\t ' + italian_dishes[i])

  print()
  print("===========================================")
  print()

  return

# If the user says yes to ordering a second dish

if yesorno == "Y":
  menufunction()

  print("Please choose a dish by indicating a code provided at the top of this message. A dish will be randomly selected for you if you do not select an existing dish.")
  print()

  order2 = input("What would you like to order? ==> ")
  print()

  # The user may order a Vietnamese dish

  if order2 in viet2:
    pos1 = viet2.index(order2)
    print("Okay, your order will be", order2 + ".")
    print() 
    print("***TRACE: dish", order2, "costs", vietnamese_dish_prices[pos1])
    print() 
    accum = accum + vietnamese_dish_prices[pos1]
  
  # The user may order an Italian dish
  
  elif order2 in ital2:
    pos1 = ital2.index(order2)
    print("Okay, your order will be", order2 + ".")
    print()
    print("***TRACE: dish", order2, "costs", italian_dish_prices[pos1])
    print() 
    accum = accum + italian_dish_prices[pos1]

  # If the user orders a dish that is not on the second menu, a random dish will be given to them

  else:
    import random
    randomdish = vietnamese_dishes + italian_dishes
    allprices = vietnamese_dish_prices + italian_dish_prices
    randish = (random.choice(randomdish))
    pos1 = randomdish.index(randish)
    print("Your random dish is", randish + ".")
    print()
    print("***TRACE: dish", randish, "costs", allprices[pos1])
    print() 
    accum = accum + allprices[pos1]

# The user may choose not to order a second dish

if yesorno == "N":
  print("Okay, sounds good.")
  print() 

# The user is done ordering

# The total cost will be shown below

print("Please pay the delivery driver", "$" + str(accum) + ".")
print()
print("Have a good day!")

# REFLECTION

# I spent around ten hours working on this assignment. 
# There were a lot of things I struggled to figure out, 
# such as the indexing, trace printing, and random module. 
# I honestly didn't think I could finish, but eventually 
# I got some help in the open lab and things are starting 
# to make more since. I still struggle with understanding 
# the indexing, but I did get more familiar with defining 
# functions and using if/elif statements. Overall, this 
# assignment was quite difficult but I am glad things came 
# together at the end.



  

