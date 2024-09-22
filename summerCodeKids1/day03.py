#Warmup
x = "Hello"
y = "Bye"

temp = x
x = y
y = temp
print("Warmup:")
print()
print(x)
print(y)

#Lists
'''
listName = [value1, value2, value3, etc.]

to find HOW MANY VALUES IN YOUR LIST: print(len(listName))

to indicate a value in your list: listName[index]

to change a value in your list: listName[index] = newValue

to slice a list: listName[start:end]
'''

#List methods
'''
list.append(value)
- adds the "value" to the end of the list

list.clear()
- removes all values from the list

new_list = list.copy()
- copies the list

list.count(value)
- returns the number of times "value" appears in the list

list.insert(index, value)
- inserts "value" at the "index"

list.pop(index)
- removes the value at the "index"

list.remove(value)
- removes the first instance of "value"

list.reverse()
- reverses the order of the list

list.sort()
- sorts the list in ascending order, or in alphabetical order if the list contains strings

list.sort(reverse=True)
- sorts the list in descending order, or in reverse alphabetical order if the list contains strings

print(sorted(list))
- prints a sorted copy of the list

'''

mixed = ['orange', 3, 1, 'apple', 5, 'banana']

fruits = []
fruits.append(mixed[0])
fruits.append(mixed[3])
fruits.append(mixed[5])
fruits.sort(reverse = True)
nums = []
nums.extend(mixed[1:3])
nums.append(mixed[4])
nums.sort()
print(fruits, nums)

############
dairyProducts = [1, 3, 4]
dairyProducts.reverse()
print(dairyProducts)

###########
test = [mixed + dairyProducts]
print(test)

my_list = ['a','1','c','3','2','b']
my_list.sort()
print(my_list)
print()