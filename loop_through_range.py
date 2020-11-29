# Loop through range

values = range(1,10)
print(values)
print(type(values))

for i in range(1,10):
    print(i)

for i in range(5):
    print(i)

for i in range(2,11,2):
    print(i)

word = "Hello World"

list_word = list(word)
print(word)
print(list_word)

list_word[5] = "New"

print(list_word)

new_word = "".join(list_word)
print(new_word)

#List and range methods
numbers = list(range(10,101,10))
print(numbers)

for number in numbers:
    print(number)

squares = []
for numb in numbers:
    square = numb**2
    squares.append(square)

print("populating squares complete")
print(squares)

for num in squares:
    print(num)

#list comprehension
cubes =[num**3 for num in numbers]
for cube in cubes:
    print(cube)

print(min(cubes))
print(max(cubes))
print(sum(cubes))

