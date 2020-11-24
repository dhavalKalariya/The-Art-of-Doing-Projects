#Looping through a list of Elements with a for loop

teams = ["Dhaval","Ritu","Pooja","Payal"]

print(teams)

print(type(teams))

#print each attribute
print(teams[0].title())
print(teams[1].title())
print(teams[2].title())
print(teams[3].title())

#Using the loop print each elements
for i in teams:
    print(i.title())
    print("you are going to win the superbowl "+i+".")

print("Go football!!")

#Nested for loop

triples = [["banana","Apple","oranges"],["dog","elephant","cow"],["parrot","sparrow","pegion"]]

for list_value in triples:
    for element in list_value:
        print(element,end= " ")
    print("\nI just finished with one of the inner loops")
    

print("I am outside of the for loops")