# Multiplication and Exponent Table

#welcome message

print("Welcome to the Multiplication/Exponent Table App")

#Get the name and the number
name = input("\nHello, What is your name:\t\t")
number = float(input("What number would you like to work with:\t"))

#Multiplication

print("\nMultiplication Table For "+str(number))

b = number

print("\n\t"+str(1.0)+" * "+str(b)+" = "+str(1.0*b))
print("\t"+str(2.0)+" * "+str(b)+" = "+str(2.0*b))
print("\t"+str(3.0)+" * "+str(b)+" = "+str(3.0*b))
print("\t"+str(4.0)+" * "+str(b)+" = "+str(4.0*b))
print("\t"+str(5.0)+" * "+str(b)+" = "+str(5.0*b))
print("\t"+str(6.0)+" * "+str(b)+" = "+str(6.0*b))
print("\t"+str(7.0)+" * "+str(b)+" = "+str(7.0*b))
print("\t"+str(8.0)+" * "+str(b)+" = "+str(8.0*b))
print("\t"+str(9.0)+" * "+str(b)+" = "+str(9.0*b))
print("\t"+str(10.)+" * "+str(b)+" = "+str(10.0*b))

#Exponent Table

print("\nExponent Table For "+ str(number))


print("\n\t"+str(b)+" ** "+str(1.0)+" = "+str(round((b**1.0),4)))
print("\t"+str(b)+" ** "+str(2.0)+" = "+str(round((b**2.0),4)))
print("\t"+str(b)+" ** "+str(3.0)+" = "+str(round((b**3.0),4)))
print("\t"+str(b)+" ** "+str(4.0)+" = "+str(round((b**4.0),4)))
print("\t"+str(b)+" ** "+str(5.0)+" = "+str(round((b**5.0),4)))
print("\t"+str(b)+" ** "+str(6.0)+" = "+str(round((b**6.0),4)))
print("\t"+str(b)+" ** "+str(7.0)+" = "+str(round((b**7.0),4)))
print("\t"+str(b)+" ** "+str(8.0)+" = "+str(round((b**8.0),4)))
print("\t"+str(b)+" ** "+str(9.0)+" = "+str(round((b**9.0),4)))
print("\t"+str(b)+" ** "+str(10.0)+" = "+str(round((b**10.0),4)))

#print fun statement

statement = name + " Math is cool!"

print("\n"+statement)
print("\t"+statement.lower())
print("\t\t"+statement.title())
print("\t\t\t"+statement.upper())

