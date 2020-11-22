#Temprature Conversion App

#Welcome message
print("Welcome to the Temprature Conversion Program")

#gather the input
temp = float(input("\nWhat is the given temprature in degrees Fahrenheit: "))

#Convert the fagreneheit to celsius and kelvin
fahreneheit = temp
Celsius = round(((fahreneheit - 32)*(5/9)),4)
kelvin = round(Celsius + 273.15,4)


#Print the results
print("\nDegree Fahreneheit:\t "+str(fahreneheit)+"\n"+"Degree Celsius:\t\t "+str(Celsius)+"\n"+"Degree Kelvin:\t\t "+str(kelvin))
