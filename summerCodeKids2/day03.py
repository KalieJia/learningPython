'''
############################################################
celsTemp = float(input("Enter a temperature in Celsius: "))

def tempConverter(celsTemp):
  fahrTemp = (celsTemp * 9/5) + 32
  return fahrTemp
print(tempConverter(celsTemp),  " is the temperature ",  str(celsTemp),  "in Fahrenheit")

############################################################
#CHECK SOLUTION 2!
def trueOrFalse(list):
  for i in range.list:
    if list[i] >= list[i-1]:
      return True
    i += 1
    else
      return False

############################################################
integer = int(input("Enter an integer: "))
def is_self_divisior(integer):
 for digit in number:
   if number % digit != 0:
     return False
  return True

print(is_self_divisor(integer))


############################################################
studentAnswerList = ["A", "A", "B", "C", "D", "A", "C", "B", "D", "A"]
answerKeyList = ["A", "A", "C", "C", "D", "D", "C", "B", "D", "A"]
def grader(studentAnswerList, answerKeyList):
  if len.studentAnswerList != len.answerKeyList:
    return "Error"
  correctAnswers = 0
  for i in range.studentAnswerList:
        if studentAnswerList[i] == answerKeyList[i]:
          correctAnswers += 1
        i += 1
    

  percentGrade = correctanswers / totalquestions * 100
  return percentGrade

print(grader(studentAnswerList, answerKeyList))

############################################################

import random 

correctint = random.randint(1, 100)
guessNum = 0

guess = input("Enter a number from 1 to 100: ")

if guess == correctint:
  print("You guessed the correct number!")
  guessNum += 1

elif guess != correctint:
  while guess != correctint:
    print("You guessed the wrong number! Try again!")
    guess = input("Enter a number from 1 to 100: ")
  guessNum +=1

############################################################
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
def angarams(word1, word2):
  sort.(str(word))
  sort.(str(word2))
  if sorted(word1) == sorted(word2):
    return "They are anagrams!"
  else:
    print("They are not anagrams!")

print(angarams(word1, word2))

#############################################################
bananas = ["white" , "yellow" , "green" , "brown" , "black", "yellow"]
def noDupes(list):
  for i in range(list):
    if list.count(list[i]) > 1:
      print("index", i, "is repeated!")
    i += 1

print(noDupes(bananas))

'''
#############################################################

base = int(input('Enter base: '))
hight = int(input('Enter height: '))

def area(base, hight):
  area = (base * hight) / 2
  return area

print("The area of your triangle is ", area(base, hight))

############################################################

import math
a = input("Enter a number: ")
b = input("Enter another number: ")
def pythagorean(a, b):
  squareOfc = a **2 + b ** 2
  return math.isqrt(squareOfc)
print(pythagorean(a, b))

#This is homework
#############################################
celsius = float(input("Enter temperature in celsius: ")) 
def celsToFahr(celsTemp):
  fahrTemp = (celsTemp * 9/5) + 32
  return fahrTemp

print("...that is the same as", celsToFahr(celsius), "in fahrenheit!")
#############################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 19, 10]
def increaseChecker(list):
  for i in range(0, len(list)-1):
    if list[i+1] < list[i]:
      return False
    return False
    
print(increaseChecker(nums))
#############################################
theNumber = int(input("Enter a number: "))
def selfDivisors(integer):
  digits = str(integer)
  for digit in digits:
    if int(digit) == 0:
      return False
    elif integer % int(digit) != 0:
      return False
  return True
print("Is this integer divisible by each of its digits:", selfDivisors(theNumber))
#############################################
KalieAnswers = ["A", "C", "D", "D", "B", "A", "B", "C", "D"]
TeacherAnswers = ["A", "C", "E", "C", "B", "A", "B", "C", "D"]

def testGrader(studentAnsList, realAnsList):
  correctAnswers = 0
  totalAnswers = len(studentAnsList)
  for i in range(totalAnswers):
      if studentAnsList[i] == realAnsList[i]:
        correctAnswers += 1
            
  percentageGrade = (correctAnswers/totalAnswers) * 100
  return percentageGrade
  return "The test cannot be graded."

print(testGrader(KalieAnswers, TeacherAnswers))
#############################################
import random
n = random.randint(1,100)
print(n)
numGuesses = 0

while True:
  guess = int(input("Guess a number from 1 to 100: "))
  numGuesses += 1
  if guess == n:
    print("Correct! The mystery number was", n, "and it took you", numGuesses, "guesses to get it!")
    break
  elif guess < n:
      print("Your guess is too low. Try again!")
  elif guess > n:
      print("Your guess is too high. Try again!")
#############################################
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
def anagramChecker(string1, string2):
  if sorted(string1) == sorted(string2):
    return True
  else:
    return False

print(string1, "and", string2, "are anagrams?", "answer:", anagramChecker(string1, string2
##############################################
def no_dupes(aList):
  resultLIst = []  
  for item in aList
    if list.count(aList[i]) > 1:
      list.pop(i)
    i += 1
    return aList

print(no_dupes([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])