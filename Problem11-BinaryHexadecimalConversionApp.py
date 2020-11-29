#Binary Hexadecimal Conversion App

#print the welcome message
print("\nWelcome to the Binary/Hexadecimal Converter App")

#gather the input for the total decimal number
End_range = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimals = list(range(1,End_range+1)) # +1 to include the last number
print("Generating lists....complete!!")
binary = []
hexadecimal = []
for num in decimals:
    binary.append(bin(num))
    hexadecimal.append(bin(num))

# for slicing, we need 2 variable for start and stop value
print("\nUsing slices, we will now show a portion of each list.")

start_decimal = int(input("What decimal number would you like to start at: "))
stop_decimal = int(input("What decimal number would you like to stop at: "))

#For decimal loop print use start and stop variable for slicing in for loop
print("\nDecimal values from "+str(start_decimal)+ " to "+ str(stop_decimal)+":")
for decimal in decimals[start_decimal-1:stop_decimal]:
    print(decimal)

#For Binary numbers using bin functions to convert to Binary
print("\nBinary values from "+str(start_decimal)+" to "+str(stop_decimal)+":")
for binary in decimals[start_decimal-1:stop_decimal]:
    binary_value = bin(binary)
    print(binary_value)

#For Hexadecimal value using hex functions to convert to hexadecimal
print("\nHexadecimal values from "+str(start_decimal)+" to "+str(stop_decimal)+":")
for hexa in decimals[start_decimal-1:stop_decimal]:
    hexa_value = hex(hexa)
    print(hexa_value)

input("\nPress Enter to see all values from 1 to "+str(End_range)+".")
print("Decimal----Binary----Hexadecimal")
print("-----------------------------------------------------------------------------")

#for loop for all the 40 numbers
for decimal in decimals:
    print(str(decimal)+"----"+str(bin(decimal))+"----"+str(hex(decimal)))

