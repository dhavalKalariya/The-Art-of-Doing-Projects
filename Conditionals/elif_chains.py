#Elif chains

age = int(input("what your age: "))

if age<18:
    print("\nyou are only "+str(age)+"!!")
    print("you can't gamble")
elif age<21:
    print("okay you are at "+str(age)+"!")
    print("YOu can play blackjack but can't have a drink")
else:
    print("\nOkay you can play blackjack and can have a drink")