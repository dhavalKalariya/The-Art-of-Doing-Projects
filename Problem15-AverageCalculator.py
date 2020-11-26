# Average Calculator

print("Welcome to the Average Calculator App")
#Get the User input
name = input("\nWhat is your name: ").title()
gradeNum = int(input("How many grades would you like to enter: "))

#Empty list to store the input values
realGrade = []

#loop the input values and append to the list
for i in range(gradeNum):
    num = int(input("Enter grade: "))
    realGrade.append(num)

sorted_realGrade = sorted(realGrade,reverse=True)

print("\nGrades Highest to Lowest: ")

#print sorted elements from highest to lowest
for i in range(len(realGrade)):
    print("\t"+str(sorted_realGrade[i]))

originalAverage = float(sum(sorted_realGrade)/len(sorted_realGrade))
originalAverage = round(originalAverage,2)

#Print the grade summary
print("\n"+str(name)+"'s Grade Summary: ")
print("\tTotal Number of Grades: "+str(gradeNum))
print("\tHighest Grade: "+str(sorted_realGrade[0]))
print("\tLowest Grade: "+str(sorted_realGrade[gradeNum-1]))
print("\tAverage: "+str(originalAverage))


#get the user input for dsired average
desiredAverage = float(input("\nWhat is your desired average: "))

print("\nGood luck "+str(name)+"!")

# originalAverage minus DesiredAverage and multiply by the number of grade and added that value to the smallest grade
requiredGrade = float(sorted_realGrade[gradeNum-1])+float((desiredAverage-originalAverage)*len(sorted_realGrade))
requiredGrade = round(requiredGrade,2)
#print a summary
print("\nYou will need to get a "+str(requiredGrade)+" on your next assignment to earn a "+str(desiredAverage)+ " average.")

#Make a copy of the original grades and swap out one of the grades

new_grades = realGrade[:]
print("\nLets see what you average could have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change) 

new_grade = int(input("What grade would you like to change from "+str(grade_change)+" to: "))
new_grades.append(new_grade)

sorted_new_grades = sorted(new_grades,reverse=True)

print("\nGrades Highest to Lowest: ")

#print sorted elements from highest to lowest
for i in range(len(sorted_new_grades)):
    print("\t"+str(sorted_new_grades[i]))

#calculate the average
new_average = float(sum(new_grades)/len(new_grades))
new_average = round(new_average,2)

print("\n"+str(name)+"'s New Grade Summary: ")
print("\tTotal Number of Grades: "+str(gradeNum))
print("\tHighest Grade: "+str(sorted_new_grades[0]))
print("\tLowest Grade: "+str(sorted_new_grades[gradeNum-1]))
print("\tAverage: "+str(new_average))

print("\nYour new average would be a "+str(new_average)+" compared to your real average of "+str(originalAverage)+" !")
average_change = new_average - originalAverage
average_change = round(average_change,2)
print("That is a change of "+str(average_change)+ " points!")

#too bad the original grades are still same
print("\nToo bad your original grades are still the same!")
print("\Please ask for the extra credits")