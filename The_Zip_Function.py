#The Zip functions

names = ["Dhaval","Ritu","Pooja","Payal"]
numbers = [10,20,30,40]

#Not the best way to print 
for name in names:
    print(name)
for number in numbers:
    print(number)

#Lets look at this another way
for i in range(len(names)):
    print(names[i].title()+" : "+str(numbers[i]))

#Using the Zip function
for name,number in zip(names, numbers):
    print(name.title()+" : "+str(number))