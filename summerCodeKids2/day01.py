''' SOME BUILT-IN FUNCTIONS
abs(x)
- returns the absolute value of x

max()
- returns the largest value in a list

min()
- returns the smallest value in a list

sum([x, y, z])
- returns the sum of the values in a list
'''

'''
Format for a math module: import and syntax

import moduleName
moduleName.method(parameter)

'''

'''MATH MODULES

math.ceil(x)
- rounds up the float of x

math.floor(x)
- rounds down the float of x

math.sqrt(x)
- returns the square root of x

math.isqrt(x)
- returns the square root of x rounded down

RANDOM MODULE
random.randint(x, y)
- returns a random integer between x and y

random.choice(list) OR random.choice(string)
- returns a random item from a list
- OR returns a random letter from a string

random.shuffle(list)
- shuffles the items in a list
'''

import math
num = 5.9
print(math.sqrt(num))
print(math.ceil(num))
print(math.floor(num))

import random
#print(random.choice("skibidi", "ohio rizz"))
print("I will eat a " + random.choice(["apple", "banana", "orange"]) + " at breakfast today.")

'''
ACCESSING CHARACTERS IN A STRING
string = "Hello"
print(string[indexNumber])

* just like a list, the index number starts at 0!

SLICING STRINGS
* characters' positions are indicated by indexes.

string[startINDEX:endINDEX]

'''

import string
'''
len(str)
- lenghth/amount of characters in a string

str.count(str2)
- returns the amount of times str2 appears in str

str.upper()
- returns a string with all uppercase letters

str.lower()
- returns a string with all lowercase letters

str.index(str2)
- returns the index number of the first occurence of str2 in str
'''

str = "Hello World"
print(str)
len(str)
print(str.count("a"))
print(str.index("l"))

print(str[2:5])


#Exercise 1
print("Your dice role was:")
print(random.choice([1, 2, 3, 4, 5, 6]))


#Exercise 2
str_list = ["apple", "banana", "orange", "mango", "strawberry"]
print("The longest word in the list is " + max(str_list))

#Exercise 3
listInt = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print("The average of listInt is:")
print(sum(listInt) / len(listInt))

#This is homework
#Exercise 4
import string
sentence = input("Enter a sentence: ")
numWords = sentence.split()
print("The number of words in the sentence is", len(numWords), ".")

#Exercise 5
print("The word 'immutable' means that the property of strings cannot be changed.")

#Exercise 6
string = "babyshark"
print(string.upper())