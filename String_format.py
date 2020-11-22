#String format

name = "Dhaval"
age = 30
money = 50.3

#print using string concatenation
print(name + " is "+ str(age) + " and has $"+str(money)+" dollars.")


#Print using .format() method
print("{0} is {1} and has ${2} dollars.".format(name,age,money))

#print using f-string
print(f"{name} is {age} and has ${money} dollars.")
