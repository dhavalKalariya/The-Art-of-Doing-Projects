#Right Tringle Solver App

import math

#Welcome Message
print("Welcome to the Right Tringle Solver App")

#Gather the input of the both legs of triangle
f_leg = float(input("\nWhat is the first leg of the triangle:\t "))
s_leg = float(input("What is the second leg of the triangle:\t "))

#Hypotenuse formula calculator
hypotenuse = round((((f_leg ** 2) + (s_leg ** 2)) ** 0.5))

#Calculate area for Triangel
#three sides of the triangle
a = f_leg
b = s_leg
c = hypotenuse

#calculate the semi-parameter for the formula
s = (a + b + c)/2

#area formula using a,b,c, and s
area = round(((s*(s-a)*(s-b)*(s-c)) ** 0.5),3)

#Print the results with statement
print("\nFor a triangle with legs of "+str(f_leg)+" and "+str(s_leg)+" the hypotenuse is "+str(hypotenuse)+".")
print("For a triangle with legs of "+str(f_leg)+" and "+str(s_leg)+" the area is "+str(area)+".")


