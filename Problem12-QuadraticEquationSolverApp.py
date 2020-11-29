#Quadratic Equation Solver App

import cmath    #To allow the complex math

print("Welcome to the Quadratic Solver App")

print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj \nWhere a is the real portion and bj is the imaginary problem.")

#get user input
eq_num = int(input("\nHow many equation you would like to solve today: "))

#Loop through to solve each equation
for i in range(eq_num):
    print("\nSolving equation #"+str(i+1)) #to start the number count from 1
    print("---------------------------------------------")
    a = float(input("\nPlease enter the value of a(coefficient of x^2): "))
    b = float(input("\nPlease enter the value of a(coefficient of x): "))
    c = float(input("\nPlease enter the value of a(coefficient): "))

    #solving the uadratic formula
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    print("\nThe solutions to "+str(a)+"x^2 +"+str(b)+"x +"+str(c)+ " = 0 are: ")
    print("\n\tx1 = "+str(x1))
    print("\tx2 = "+str(x2))

print("\nThank you for using the quadratic equation solver app")
print("Good Bye")