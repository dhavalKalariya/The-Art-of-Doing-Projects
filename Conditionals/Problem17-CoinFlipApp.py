#Coin Flip App

import random

print("Welcome to the Coin Flip App")

print("\nI will flip a coin a set number of times.")

number = int(input("\nHow many times would you like me to flip the coin: "))

heads = []
tails = []
flips = []

for i in range(1,number+1):
    #fliping coin using random library
    flip = random.randint(0,1)
    
    if flip == 1:
        heads.append("Head")
        print("Head")
    else:
        tails.append("Tail")
        print("Tail")

    headcount = len(heads)
    tailcount = len(tails)
    
    if headcount == tailcount:
        print("At "+str(i)+" flips, the number of heads and tails were equal at "+str(i/2)+ " each")

#calculate percantages
heads_percentage = round(100*headcount/number,2)
tails_percentage = round(100*tailcount/number,2)

    
print("Results of Flipping A Coin "+str(number)+" Times:")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t"+str(headcount)+"/"+str(number)+"\t\t"+str(heads_percentage)+"%")
print("Heads\t\t"+str(tailcount)+"/"+str(number)+"\t\t"+str(tails_percentage)+"%")



