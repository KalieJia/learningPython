    #Exercise
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numList[0])
print(numList[9])

print(numList[2:6])

numList.sort(reverse=True)
print(numList)

# User input
name = input("Enter your name: ")
# Input always stores a string!
print("Hello, " + name)

products = ["apple", "pear", "orange"]
is_there_apple = "apple" in products
print(is_there_apple)

#conditionals
if 3 > 2:
  print("3 is greater than 2")
print("if statement complete")

grades = [90, 87, 65, 100, 79]
if 100 in grades:
  print("You got a perfect score!")
else:
  print("U R Bad")

number = input("your number: ")
if int(number) % 2 == 0:
  print("even")
else:
  print("odd")

#Exercise for practice
#1
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
if int(num1) % int(num2) == 0:
  print("The first number is divisible by the second number")
else:
  print("the second number is not a factor of the first number")

#2
grade = input("Enter your grade: ")
if int(grade) >= 90 and int(grade) <= 100:
  print("It's an A")
elif int(grade) >= 80 and int(grade) <= 89:
  print("It's a B")
elif int(grade) >= 70 and int(grade) <= 79:
  print("It's a C")
if int(grade) >= 60 and int(grade) <= 69:
  print("It's a D")
if int(grade) >= 0 and int(grade) <= 59:
  print("It's an F. You failed! :<")

#3
color = input("Enter a color: ")
if color == "red" or color == "blue" or color == "white":
  print("It's a U.S. flag color!")
else:
  print("It's not a U.S. flag color")
'''
#4
fahrenheitTemp = input("Enter a temperature in Fahrenheit: ")
if fahrenheitTemp <= -32:
  print(fahrenheitTemp + " is solid!")
elif fahrenheitTemp <= 212:
  print(fahrenheitTemp + " is liquid!")
else:
  print(fahrenheitTemp + " is gas!")
  '''

#5
subjects = ["math", "science", "english", "history"]
newsubject = input("Enter school subject: ")
if newsubject in subjects:
  print("That's already on the list!")

else:
  subjects.append(newsubject)
  print("way to go! that's one i didn't think of!")

print(subjects)