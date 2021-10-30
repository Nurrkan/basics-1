# 10/30/2021  CHAPTER 4
## Lists: Looping

cars = ['bmw', 'tesla', 'lexus', 'ferrari']
# a +b will not work here since it is defined in the next lines
"""
for tempVariable in iterativeOjbects: 
    code here using tempVariable

in Java: 
    for car in cars {
        print(f"I love {car} a lot!")
        print("heey!")
    }
for item in list_of_items:    
"""

for car in cars:
    print(f"I love {car} a lot!")
    # print(f"I love {cars} a lot!")
    print("heey!")

# scope of car variable is inside for loop block
print(f"this is my hobby.{car}")  ## this is not right way of using
print("woooooww!")

a = 1
b = 2

print("########  4-1: Pizzas #######################")
pizzas = ['pepperoni', 'mushroom', 'cheese', 'grandma']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizzaaaaaaaaaaaaaaaaaa!!!!!!")

### shortcut: ctrl(cmd) + alt + l > to autoformat code on current file:
# shortcut : ctrl + d > duplicating the line that your cursor on
# shortcut : ctrl + y > delete the line that  your cursor on
# shortcut: shift + alt(cmd) + up/down > dragging and dropping the line

print("########  4-2: Animals #######################")

animals = ['cat', 'dog', 'horse']
for animal in animals[:1]:
    print(f"A {animal} will make a great pet!")
print("Any of these animals would make a great pet!")

# slicing the list name_of_list[startIndex:endIndex]
#   - this means creating subList from startIndex element (inclusive) to endIndex-1 (excluding endIndex element)
# name_of_list[:] - from the start to end of the list

print("########### copying the list #####################")
new_animals = animals  ## this is not copying the list
print(f"copy_animals list: {new_animals}")
print(f"animals list: {animals}")
new_animals.append('snake')
print("added snake to new_animals")
print(f"copy_animals list: {new_animals}")
print(f"animals list: {animals}")
## in this case we are creating 2 references to the same list in the memory
print("######## copying with [:] ##### ")
copy_animals = animals[:]
# you can copy part of the list as well like animals[1:3] - only 2 elements
print(f"copy_animals list: {copy_animals}")
print(f"animals list: {animals}")
copy_animals.append('alligators')
print("added alligator to the copy_animals")
print(f"copy_animals list: {copy_animals}")
print(f"animals list: {animals}")

print("################## Making Numerical Lists ############")
# range(start, stop, step)
# range(stop)
# range(start, stop)
for num in range(6, 15, 3):
    print(num)

print("# print the numbers from 20-50 dividable by 3")
for num in range(21, 51, 3):
    print(num)
nums_by_3 = list(range(21, 51, 3))  # or nums_by_3 = [range(21, 51, 3)]
print(nums_by_3)

print("#### print the squares of numbers between 10-20")
squares = []
for num in range(10, 21):
    print(num * num)  # or    print(num**2)
    print(num * num * num)  # or    print(num**3)
    squares.append(num ** 2)
print(squares)

print("$$$$$$$$$$$ Statistics $$$$$$$$$$$$$$$")
print(f"min of squares: {min(squares)}")
print(f"max of squares: {max(squares)}")
print(f"sum of squares: {sum(squares)}")

print("####### List Comprehensions  #####################")
squares = [num ** 2 for num in range(5, 10)]
print(squares)

## range(1, 20, 2)
odds = [num for num in range(1, 20, 2)]
print(odds)
### H/w: from 4-3 ot 4-9
### H/w: from 4-10 ot 4-12

# Data structrues:
### lists - mutable object - you can modify object(list)
### tuple - immuatable object - you can not modify this object(tuple)

# PEP 8 - code styling standards for python, when you do autoformat pycharm applies PEP 8 standard rule (blanks, empty lines, etc.)
