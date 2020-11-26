# Fibonacci Calculator App

import math
import cmath

print("Welcome to the Fibonacci Calculator App.")

#get the user input
number = int(input("\nhow many digits of fibonacci sequence would you like to compute: "))

#compute the value of fib
print("\nThe first "+str(number)+" number of the Fibonacci sequence are:")

#starting 2 variable
fibonacci = [1,1]

#for loop for the fibonacci
for i in range(number-2): #here we already took 2 variable in starting therefore reducing that many from the original number
   nextElement =  fibonacci[i] + fibonacci[i+1]
   fibonacci.append(nextElement) #add the number in the fibonacci list

#for loop to print each elements of fibonacci list
for num in fibonacci:
    print(num)

#Compute the golden ratio 
print("\nThe corrensponding Golden ratio values are: ")
golden = []
for i in range(len(fibonacci)-1): #Number of ratios will be less by 1
    ratio = fibonacci[i+1]/fibonacci[i]
    golden.append(ratio)

for j in golden:
    print(j)

print("\nThe ration of consecutive Fibonacci terms approaches Phi; 1.618....")


