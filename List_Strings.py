#List Strings

numbers = list(range(1,11))

for num in numbers:
    print(num)

#Slicing
print("\nSlicig")
for num in numbers[0:5]:
    print(num)

#How NOT to do copy

new_numbers = numbers
print(new_numbers)
print(numbers)

#Both will so the same result even if the elements remove from numbers list
numbers.pop()
print(numbers)
print(new_numbers)

# how to do the copy
numbers = list(range(1,6))
print(numbers)

new_numbers = numbers[:]
print(new_numbers)

#the number will pop out only from numbers but not from new_numbers
numbers.pop()
print(numbers)
print(new_numbers)

#Copy Methods
names = ["Dhaval","Ritu","Pooja","Payal"]
new_names = names.copy()
print(names)
print(new_names)

new_names[0] = new_names[0].upper()

print(names)
print(new_names)

