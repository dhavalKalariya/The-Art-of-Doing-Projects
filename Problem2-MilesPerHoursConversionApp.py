# Convert Miles per Hours Conversion App

#Welcome Message
print("Welcome to the MPH to MPS Conversion App")

#taking the input
speedinmile = float(input("\nWhat is your speed in miles per hour: "))

#Formula to convert from Mile per hour to Meter in seconds
result = round(float(((speedinmile*1609.34)/3600)),2)

#Print the result
print("Your speed in meters per second is " + str(result) + ".")
