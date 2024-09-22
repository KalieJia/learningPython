#practice problem: diceroll simulator
import random
rolls = []
def dice(times):
  for i in range(times):
    rolls.append(random.randint(1,6))
  return rolls

times = int(input("How many times do you want to roll the dice? "))
dice(times)
print(*rolls)

def nothing():
  pass

#Exercise 1
def count_digits(num,digit):
  
  number = str(input("Enter a number: "))
print()


#DICTIONARY SYNTAX:
dictionary = {
  "key_1" : "value_1",
  "key_2" : "value_2",
  "key_3" : "value_3"
}
'''
money = {
  "Kalie": [50, -15, 36, -7]
  "Karen": [100, -10, -5, -5]
  "Kangbin": [25, -5, 10, 20]
}
'''
def function(dictionary, targetValue):
  for key in dictionary:
    print(key)
    print(dictionary[key])

print(dictionary.get("key_1"))
print(dictionary.get("hi"))
print(dictionary.get("hi", 0))
print(len(dictionary))

#exercise: rename key
oldKey = input("Enter a key you want to replace: ")
newKey = input("Enter a key you want to replace: ")
def renameKey(dict, oldKey, newKey):
  dict[newKey] = dict.pop(oldKey)
  return dict

print(dictionary)

#Exercise: lists to dictionary
'''
def listToDict(listOfKeys, listOfValues):
    dic = {}
    for i in range(len(listOfKeys)):
      dic.append(listOfKeys[i] : listOfValues[i])
      i += 1
if len(listOfKeys) == len(listOfValues):
  print(listToDict())

else:
  return "Dictionary not possible"
'''
#Exercise: Is Empty
def emptyOrNot(dictionary):
  if len(dictionary) == 0:
    print(True)
  else:
    print(False)
emptyOrNot(dictionary)

#This is homework
import random

name = input("What is your name? Enter it here: ")
def greet(name):
  print("Hello, " + name + "!")

print(greet(name))

#######################

roll_Times = int(input("How many times do you want to roll the dice? Enter it here: "))

def roll_dice(roll_Times):
  diceRolls = []
  for i in range(roll_Times): 
    roll = random.randint(1,6)
    diceRolls.append(roll)
    i += 1

  return diceRolls
  
print(roll_dice(roll_Times))

#######################

num = input("Enter a number: ")
digit = input("Enter a digit: ")

def count_digits(num, digit):
  print(num.count((digit)))
  return print("The digit " + str(digit) + " appears " + str(num.count(digit)) + " times in your number.")

if len(digit) != 1:
  print("Please enter a single digit.")
else:
  print(count_digits(num, digit))


#######################
oneToHundred = list(range(1,101))
def multipleReplacer(oneToHundred):
  
  for i in range(len(oneToHundred)):
    if oneToHundred[i] % 3 == 0 and oneToHundred[i] % 5 == 0:
      oneToHundred[i] = "FizzBuzz"

    elif oneToHundred[i] % 3 == 0:
      oneToHundred[i] = "Fizz"

    elif oneToHundred[i] % 5 == 0:
      oneToHundred[i] = "Buzz"

  print(oneToHundred)


multipleReplacer(oneToHundred)
print(oneToHundred)

#######################
import random
word = "boat"
def scramble(word):
  letters = []
  for letter in word:
    letters.append(letter)
  random.shuffle(letters)
  result_str = ""
  for letter in letters:
    result_str += letter
  return result_str
  
print("Unscramble this word: ", scramble(word))
  #The User's Guess!
userGuess = input("Enter your guess: ")
if userGuess == word:
  print("You got it right!")

else:
  print("You got it wrong. The word was" + word)

#######################
numbersOnly = [2, 234, 3456, 78, 4, 6546, 23, 9]
def whatIsTheRange(list):
 if str or bool in numbersOnly:
   print("the list can ONLY have numbers!")
 else:
    print(max(numbersOnly) - min(numbersOnly))
  
print(whatIsTheRange(numbersOnly))

#######################
num = input("Enter a number: ")
def digitSum(num):
  sum = 0
  for digit in str(num):
    sum += int(digit)
  return sum
print("The sum of the digits is", digitSum(num))

#######################
someNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def coolOrNot(list):
  for i in range(len(list)):
    if list[i] % 2 == 0:
      return "Cool"
    else:
      return "Not Cool"

print(coolOrNot(someNums))

##########################
#the syntax:
'''
dictionary = {
  "key": "value",
  "key2": "value2",
  "key3": "value3"
}
'''
num1 = int(input("Choose a number from 0 to 2: "))
num2 = int(input("Choose a number from 0 to 2: "))
num3 = int(input("Choose a number from 0 to 2: "))
num4 = int(input("Choose a number from 0 to 2: "))
num5 = int(input("Choose a number from 0 to 2: "))
num6 = int(input("Choose a number from 0 to 2: "))
analogies = {
  "boat" : ["ocean", "river", "lake"],
  "bird" : ["sky", "nest", "tree"],
  "car" : ["road", "driveway", "garage"],
  "cow" : ["pasture", "farm", "wild"],
  "dog" : ["house", "field", "backyard"],
  "butterfly" : ["garden", "milkweed", "forest"]
}
if type(num1) == str or type(num2) == str or type(num3) == str or type(num4) == str or type(num5) == str or type(num6) == str or type(num1) == bool or type(num2) == bool or type(num3) == bool or type(num4) == bool or type(num5) == bool or type(num6) == bool or num1 > 3 or num2 > 3 or num3 > 3 or num4 > 3 or num5 > 3 or num6 > 3 or num1 < 1 or num2 < 1 or num3 < 1 or num4 < 1 or num5 < 1 or num6 < 1:
  print("Please enter a number from 1 to 3.")

print("boat : ", analogies["boat"][num1])
print("bird : ", analogies["bird"][num2])
print("car : ", analogies["car"][num3])
print("cow : ", analogies["cow"][num4])
print("dog : ", analogies["dog"][num5])
print("butterfly : ", analogies["butterfly"][num6])

analogies["human"] = ["everywhere", "everywhere!"]
analogies["human"].append("everywhereAgain")

print("ANALOGIES LIST: ", analogies)

############################################ Using same dictionary as before

def extractor(dictionary, target_value):
  for key in dictionary:
    if dictionary[key] == target_value:
      return key
    else:
      return str(target_value) + " is not in this dictionary"
print(extractor(analogies, analogies.get("boat")[1]))
print("bird" in analogies)
print(len(analogies))
del analogies["dog"]
print(analogies)
items_list = analogies.keys()
print(items_list)
values_list = analogies.values()
print(values_list)
newChange = {"bird" : "antarctica"}
newChanges = {"human" : "airplane", "cow" : "dairy farm"}
analogies.update(newChange)
analogies.update(newChanges)
print(analogies)

################################################################
renameKeyExercise = {
  1 : "a",
  2 : "b",
  3 : "c",
  4 : "d",
  5 : "e",
  6 : "f"
}

def renameKey(dictionary, keyToBeReplaced, newKey):
  if keyToBeReplaced in dictionary:
    dictionary[newKey] = dictionary.pop(keyToBeReplaced)
    return dictionary
  else:
    return "Key not found"

print(renameKey(renameKeyExercise, 2, "z"))

######################################################################
keys = ["a", "b", "c", "d", "e", "f"]
values = [1, 2, 3, 4, 5, 6]

def listToDict(listOfKeys, listOfValues):
  newDict = {}
  if len(listOfKeys) == len(listOfValues):
    for i in range(len(listOfKeys)):
      change = {listOfKeys[i] : listOfValues[i]}
      newDict.update(change)
      i += 1
    return newDict
  else:
    return "Dictionary not possible"

print(listToDict(keys, values))

#######################################################################
testScores = {}
def emptyOrNot(dictionary):
  if len(dictionary) == 0:
    return "Dictionary is empty"
  else:
    return "Dictionary is not empty"
print(emptyOrNot(testScores))

######################################################################
rainbow = {
  1 : "red",
  2 : "orange",
  3 : "yellow",
  4 : "green",
  5 : "blue",
  6 : "indigo",
  7 : "purple"
}
def swapper(dictionary):
  swappedDict = {}
  for key in dictionary:
    value = dictionary[key]
    swappedDict[value] = key
  return swappedDict
print(rainbow)
print(swapper(rainbow))

##############################################################
inventory = {
  "apple" : 5,
  "banana" : 7,
  "pear" : 3,
  "orange" : 2,
  "grape" : 4
}

for key in inventory:
  num_items = str(inventory[key])
  print("There are", num_items, " ", key, "in my inventory.")