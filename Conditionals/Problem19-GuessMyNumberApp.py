# Guess my number app
import random

print("Welcome to the Guess My Number App")

#Gather user input
name = input("\nHello! What is your name: ").title().strip()
print("Well "+str(name)+", I am thinking of a number between 1 and 20.")

number_inmind = random.randint(1,20)

count = 0

for i in range(1,6):

    guess = int(input("\nTake a guess: "))
    if number_inmind == guess:
        count += 1
        print("\nYou guessed the correct number in "+str(count)+" count.")
        break
    elif number_inmind < guess:
        print("\nYour guess is too high")
        count += 1
    else:
        print("\nYour guess is too low")
        count += 1
    if count == 5:
        print("\nGame Over. The number I was thinking of was "+str(number_inmind)+".")

    