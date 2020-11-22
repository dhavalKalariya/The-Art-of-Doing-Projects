print("Welcome to the favorite Teachers Program")

teachers = []

#Grab the input 
teacher = input("\nWho is your first favorite teacher: ").title()
teachers.append(teacher)
teacher = input("\nWho is your second favorite teacher: ").title()
teachers.append(teacher)
teacher = input("\nWho is your third favorite teacher: ").title()
teachers.append(teacher)
teacher = input("\nWho is your forth favorite teacher: ").title()
teachers.append(teacher)

#Print the list
print("\nYour favorite teachers ranked are: "+str(teachers))
#print the sorted list
print("\nYour favorite teachers Alphabatically are: "+str(sorted(teachers)))
#print the reverse alphabatically sorted list
print("\nYour favorite teachers Reverse Alphabatically are: "+str(sorted(teachers,reverse=True)))
#print the first top 2 favorite teachers
print("\nYour top two teachers are: "+ teachers[0]+" and "+teachers[1]+".")
#print the second next top 2 favorite teachers
print("\nyour second next top two teachers are: "+teachers[2]+" and "+teachers[3]+".")
#print the last favorite teachers
print("\nYour last favorite teacher is: "+teachers[-1]+".")
#print the favorite number of teachers
print("\nYou have a total of "+str(len(teachers))+" favorite teachers.")

#Insert a new favorite teacher
teachers.insert(0,input("\nOops, "+teachers[0]+ " is no longer your favorite teachers. Who is your new favorite teacher now: ").title())

#Print the list
print("\nYour favorite teachers ranked are: "+str(teachers))
#print the sorted list
print("\nYour favorite teachers Alphabatically are: "+str(sorted(teachers)))
#print the reverse alphabatically sorted list
print("\nYour favorite teachers Reverse Alphabatically are: "+str(sorted(teachers,reverse=True)))
#print the first top 2 favorite teachers
print("\nYour top two teachers are: "+ teachers[0]+" and "+teachers[1]+".")
#print the second next top 2 favorite teachers
print("\nyour second next top two teachers are: "+teachers[2]+" and "+teachers[3]+".")
#print the last favorite teachers
print("\nYour last favorite teacher is: "+teachers[-1]+".")
#print the favorite number of teachers
print("\nYou have a total of "+str(len(teachers))+" favorite teachers.")

