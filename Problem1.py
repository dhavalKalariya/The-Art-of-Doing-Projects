#Problem 1
#Letter Counter App

print("Welcome to the Letter Counter App")

#Get User input
name = input("What is your name: ")
print("Hello "+ name.title() + "!")
print("I will count the number of times that a specific letter occurs in a message.")


message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occurences of: ")

#Standardize to lower case
message = message.lower()
letter = letter.lower()

#get the count and display the results
c_count = message.count(letter)

print(f"{name}, your message has {c_count} {letter}'s in it")
