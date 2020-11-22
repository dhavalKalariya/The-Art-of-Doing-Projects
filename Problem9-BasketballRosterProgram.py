# BasketBall Roster program

print("Welcome to the basketball Roster program")

roster = []

player = input("\nWho is your Point Guard: ").title()
roster.append(player)
player = input("Who is your Shooting Guard: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)

print("\n\t Your Starting"+str(len(roster))+" for the upcoming basketball season")
print("\n\t\tPoint Guard: \t"+roster[0])
print("\t\tShoting Guard: \t"+roster[1])
print("\t\tSmall Forward: \t"+roster[2])
print("\t\tPower Forward: \t"+roster[3])
print("\t\tCenter: \t"+roster[4])

print("\nOh no, "+roster[2]+" is injured")
injured_player = roster.pop(2)
print("Your roster only has "+str(len(roster))+" players.")
replace = input("Who will take "+injured_player+"'s spot: ").title()

roster.insert(2,replace)
print("\n\t Your Starting"+str(len(roster))+" for the upcoming basketball season")
print("\n\t\tPoint Guard: \t"+roster[0])
print("\t\tShoting Guard: \t"+roster[1])
print("\t\tSmall Forward: \t"+roster[2])
print("\t\tPower Forward: \t"+roster[3])
print("\t\tCenter: \t"+roster[4])

print("\nGood luck "+roster[2]+" you will do great!")
print("Your roster now has "+str(len(roster))+" players")