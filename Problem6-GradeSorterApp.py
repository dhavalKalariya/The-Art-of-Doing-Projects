# Grade Sorter App

#Welcome message
print("Welcome to the Grade Sorter App")

#gather the input as 4 grades
grades = []
grade = int(input("What is your first grade(0-100): "))
grades.append(grade)
grade = int(input("What is your Second grade(0-100): "))
grades.append(grade)
grade = int(input("What is your third grade(0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade(0-100): "))
grades.append(grade)

#defined grade as list
print("\nYour grades are: "+ str(grades))

#Sort the list by descending order
grades.sort(reverse=True)

print("\nYour grades from highest to lowest are: "+str(grades))

#Remove the 2 lowest grade
print("\nThe lowest two grades will now be dropped.")
print("\nRemoved grade: "+ str(grades.pop()))
print("Removed grade: "+ str(grades.pop()))

#Print the remaining grades
print("\nYour remaining grades are: "+str(grades))

#print nice work message
print("\nNice work! Your highest grade is a "+str(grades[0])+".")
