'''
#Exercise
number = input("Enter a number: ")
if int(number) > 0:
  print("The number is positive")
elif int(number) < 0:
  print("The number is negative")
else:
  print("The number is zero")

#Exercise
carbs = input("Enter the number of carbohydrates: ")
fiber = input("Enter the number of fiber: ")
if int(carbs)/int(fiber) >= 10/3:
  print("The food is high in fiber")
else:
  print("The food is not high in fiber")

#Exercise: try and except, type casting
num = input("Enter a number to square: ")
try:
  print(float(num) ** 2)
except:
  print("Please enter an actual number")

#xercise
var = []
try:
  len(var)
  print('var is a string/list')
except:
  print('var is a float/int/bool')

#type(item)
print(type(1.5))

#Exercises
string = input("Enter a string: ")
integer = input("Enter an integer: ")
try:
  print(string * int(integer))
except:
  print("Please enter a valid integer")

#LOOPS while loops
y = 1
while y < 100:
  print(y)
  y += 1

#For loops
letter = input("enter a letter: ")
for letter in "Hello":
  print(letter)

#for loops practice
num_list = [9, 0, -3, 5, 98, -47]
num_list.sort()
min = num_list[0]
for i in range(len(num_list)):
  if num_list[i] < min:
    value = num_list[i]
print(num_list)

#Exrcise 3: "break"

#Exercise 4: "continue"

#Exercise 5: Create a list of 10 integers. Use a loop to determine how many even numbers are in the list. Print the number of even numbers
'''

list = [5, 7, 23, 6, 234, 8, 345, 3235, 6, 7]
value = list[0]
while 10 > len(list) and value % 2 == 0:
  print(value)
  list.pop(0)