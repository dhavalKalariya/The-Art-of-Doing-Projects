#Shipping Accounts program

print("Welcome to the Shipping Accounts Program")

users = ["Adam","John","Kyle","Carol","Peter"]

login_user = input("Hello, what is your username: ")

for user in users:
    if login_user == user:
        print("Hello "+str(login_user)+". Welcome back to your account.")
        print("Current shipping prices are as follows: ")

        print("Shipping orders 0 to 100:\t $5.10 each")
        print("Shipping orders 101 to 500:\t $5.00 each")
        print("Shipping orders 501 to 1000:\t $4.90 each")
        print("Shipping orders more than 1000:\t $4.80 each")

        #Get the user input
        items = int(input("How many items would you like to ship: "))

        #Find the cost by number of items
        if items <= 100:
            perItem = 5.10
            cost = items*5.10
        elif items <= 500:
            perItem = 5.00
            cost = items*5.00
        elif items <= 1000:
            perItem = 4.90
            cost = items*4.90
        else:
            perItem = 4.80
            cost = items*4.80
        
        #print the cost for the ship
        print("To ship "+str(items)+" items it will cost you "+str(cost)+ " at "+str(perItem)+" per item.")

        order = input("Would you like to place this order (y/n): ")
        
        if(order == "y"):
            print("Okay, Order has been placed this time.")
        elif order == "n":
            print("Okay, no order is being placed at this time.")
        else:
            print("Please provide the correct answer of the order.")
        

if (login_user not in users):
        print("Sorry, you do not have an account with us. Goodbye!!")
        

