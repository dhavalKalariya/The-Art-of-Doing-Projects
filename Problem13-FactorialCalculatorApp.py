#Factorial Calculator App

import cmath
import math

print("Welcome to the Factorial calculator App")

#get the user input
number = int(input("\nWhat number you would like to compute the factorial of? "))

print(str(number)+"! = ",end="") #end commands to stay where the print statement ends
for i in range(1,number):
    print(str(i),end="*") #end adds the * at the end of each print statement
print(str(number))


#Using for math library
print("\nHere is the result from math library: ")
print("The factorial of "+str(number)+" is "+str(math.factorial(number))+"!")

#Using our own algorithm
fact = 1
for j in range(1,number+1):
    fact = fact * j

#Using for math library
print("\nHere is the result from Our own Algorithm: ")
print("The factorial of "+str(number)+" is "+str(fact)+"!")
