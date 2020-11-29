#Simple if/else Statement

colors = ["blue","green","yellow"]

for color in colors:
    print(color)

for color in colors:
    if color == "yellow":
        print(color.upper())
        print("I love this color")
    else:
        print(color)
        print("The color "+str(color)+" is okay...")
    
#Numerical comparison operator
age = int(input("\nWhats your age: "))
if age >=21:
    print("Have a drink")
else:
    print("Aah.. no drinks for you")

first_name = "Dhaval"
last_name = "Kalariya"
if first_name == "Dhaval" and last_name == "Kalariya":
    print("\nyou are the cool guy")
else:
    print("you are not a cool guy")

if first_name == "Dhaval" or last_name == "Kalariya":
    print("\nyou are the cool guy")
else:
    print("you are not a cool guy")