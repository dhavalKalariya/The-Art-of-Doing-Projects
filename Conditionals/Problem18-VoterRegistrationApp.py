# Voter Registration App

print("Welcome to the Voter Registration App")

#get the user input name and age
voter = input("\nPlease enter your name: ").title()
age = int(input("Please enter your age: "))

# verify if the voter is 21 year or older
if age >= 21:
    print("Congratulations "+str(voter)+"! You are old enought to register to vote.")

    print("Here is a list of political parties to join.")
    print("\t- Republican")
    print("\t- Democratic")
    print("\t- Independent")
    print("\t- Libertarian")
    print("\t- Green")

    parties = ["Republican","Democratic","Independent","Libertarian","Green"]

    voting_party = input("\nWhat party would you like to join: ").title()

    if voting_party in parties:
        if voting_party == "Repulican":
            print("\nCongratulations "+str(voter)+"! You have joined the "+str(voting_party)+" party!")
            print("That is a major party")
        elif voting_party == "Democratic":
            print("\nCongratulations "+str(voter)+"! You have joined the "+str(voting_party)+" party!")
            print("That is a major party")
        elif voting_party == "Independent":
            print("\nCongratulations "+str(voter)+"! You have joined the "+str(voting_party)+" party!")
            print("That is not a major party")
        elif voting_party == "Libertarian":
            print("\nCongratulations "+str(voter)+"! You have joined the "+str(voting_party)+" party!")
            print("That is a major party")
        elif voting_party == "Green":
            print("\nCongratulations "+str(voter)+"! You have joined the "+str(voting_party)+" party!")
            print("That is not a major party")    
    else:
        print("\nPlease vote for the correct party.")

else:
    print("\nSorry "+str(voter)+"! You are not old enough to register the vote")
