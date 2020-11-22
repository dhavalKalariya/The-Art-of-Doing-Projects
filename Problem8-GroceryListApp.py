# Lists Challenge 8: gorcery List App

import datetime

# Create the date time Oject and store current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


# Welcome message
foods = ['Meat','Cheese']
print("Welcome to the Grocery List App")
print("Current Date and time: "+month+"/"+day+"\t"+hour+":"+minute)
print("You currently have "+foods[0]+ " and "+foods[1] + " in your grocery list")

# Get user input
food = input("\nType of food to add the grocery list: ")
foods.append(food.title())
food = input("\nType of food to add the grocery list: ")
foods.append(food.title())
food = input("\nType of food to add the grocery list: ")
foods.append(food.title())

#print and sort the list
print("\nNow, here is your new grocery list: ")
print(foods)
foods.sort()
print("\n here is your grocery list sorted: ")
print(foods)

# Simulate the shopping

print("\nSimulating grocery shopping...")
print("\n\nCurrent Grocery list: "+str(len(foods))+" items")
print(foods)
buy_food = input("\nwhat food did you just buy: ").title()
foods.remove(buy_food)
print("\nRemoving "+buy_food+ " from the list")

print("\n\nCurrent Grocery list: "+str(len(foods))+" items")
print(foods)
buy_food = input("\nwhat food did you just buy: ").title()
foods.remove(buy_food)
print("\nRemoving "+buy_food+ " from the list")

print("\n\nCurrent Grocery list: "+str(len(foods))+" items")
print(foods)
buy_food = input("\nwhat food did you just buy: ").title()
foods.remove(buy_food)
print("\nRemoving "+buy_food+ " from the list")

#The store is out of an item....
print("\nCurrent grocey list: "+str(len(foods))+" items")
print(foods)
no_item = foods.pop()
print("\nSorry, the store is out of "+no_item+" .")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\n Here is what remains in the grocery list: ")
print(foods)

