# CHAPTER 5 : If statement

# yes/no (True/False) Expressions:
# 5 == 4    -> False
# 25 > 15   -> True
# 'a' in 'car'   -> True
# 'b' in 'car'   -> False
a = 20
# a == 20   -> True
# a == 30   -> False
# b.upper() == 'JOHN'
# a != 20   -> False
nums = [4, 8, 2, 90]
# 5 in nums     -> False
print(5 in nums)
print(2 in nums)

'''
if <logical expression> :
    <code to execute if logical expression is True>
else: 
    <code to execute if the expression is False>
'''
# user = input("Enter your name here: ")
user = 'joh'
if user.lower() == 'john':
    print(f"Hello, {user.title()}!!!!")
    print("What do you want to study today!")
else:
    print("Sorry I dont know you.")

print("#################### if in loops #############")
cars = ['BmW', 'Lexus', 'FerraRi', 'TesLa']

for car in cars:
    if car.lower() == 'ferrari':
        print(f"Wooow you must really love your {car.upper()}!")
    else:
        print(f"{car.title()} is a good car, good for you.")

####### 10/09/2021
## H/W: how to print multiplication table
print("############# example of Nested for loop ############")
names = ['mark', 'alex', 'john']
pizzas = ['cheese', 'pepperoni', 'chicken', 'granma']
for name in names:
    print(name)
    for pizza in pizzas:
        print(f"{name} likes {pizza}.")
    print("############################")

print("######### multiple conditions ##################")
'''
using AND , OR operators
True and True and true = True
False and true and true = False

True or True or true = True
False or true or false = true
False or False  = false

Expressions: 
a < 100 and a > 50  
b != 150 and b > 100
(car == 'ferrari') or (car == 'bentley')

% - modulo - remainder after division
    13 = 3*4 +1 >> 
    13 % 3 = 1; 13 % 4 = 1

// - floor division
    13 // 3 = 4
    13 // 4 = 3

'''
user_active = True

if user_active:
    print(f"Hello user")
else:
    print("please activate your user.")

print("########### if-elif-else statement #############")
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.
age = 4

if 4 < age <= 18:
    print('Your admission fee is $5.')
elif age <= 4:
    print('Your admission fee is free.')
else:
    print('your admission fee is $10.')

requested_toppings = ['mushrooms', 'extra cheese']
# independantly checked conditions
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

# each elif condition is checked only if previous condition is not met.
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
else:
    print('sorry we dont have the requested topping.')

print("################### 5-3 ###################")
alien_color = 'red'
if alien_color.lower() == 'green':
    print("you can just earned 5 points, Yehooo!!")
print("################### 5-5 ###################")
alien_color = 'x'
# alien_color = input('Enter the color of alien you shot: ')

while alien_color.lower() != 'exit' and alien_color.lower() != 'x':
    if alien_color.lower() == 'green':
        print("you just earned 5 points, Yehooo!!")
    elif alien_color.lower() == 'yellow':
        print("you just earned 10 points, great!!")
    elif alien_color.lower() == 'red':
        print("you just earned 15 points, well done!!")
    else:
        print('you have not earned any points, keep trying...')
    alien_color = input('Enter the color of alien you shot: ')

print("####################### 3 and 5 exercise ########################")
# create a list of numbers from 1 to 100 that can be
# dividable by 3 (listBy3),
# dividable by 5 (listBy5)
# dividable by 3 and 5 (listBy35)

listBy3 = []
listBy5 = []
listBy35 = []
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        listBy35.append(num)
    elif num % 3 == 0:
        listBy3.append(num)
    elif num % 5 == 0:
        listBy5.append(num)
    # print(num)

print(listBy3)
print(listBy5)
print(listBy35)

# H/W: FuzzBuzz exercise:
# accept the input , if you see in the input 'Fuzz' print it "Fuzz", if input "Buzz', print "Buzz", if "FuzzBuzz" print "FuzzBuzz"
# https://www.hackerrank.com/challenges/fizzbuzz/problem

### Checking for false conditions
a = 0
mylist = []  # this list will return false if it is empty

print("#################  nested lists #########################")

players = [['john', 25, 456],
           ['mark', 23, 478],
           ['jose', 30, 244]]

print(players[0][2])  # first row third column
print(players[1][1])  # second row second column

print("###### looping through this list ############ ")
for player in players:
    print(f"Name of the player: {player[0]}.")
    print(f"Age of the player: {player[1]}.")
    print(f"Score of the player: {player[2]}.")
    print("--------------------------------")

print("############################ 5-10: Checking Usernames ###############")
'''
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users. • Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list. • Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying
that the username is available. • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
'''
current_users = ['superman12', 'spiderman77', 'hulk0', 'ladybug99']
new_users = ['blackwidow', 'spiderman77', 'hulk', 'superman12']

# loop through all new_users
for new_user in new_users:
    # check each user is in the current_user list (if)
    if new_user in current_users:
        # print "You need to enter a new username"
        print(f"Username: '{new_user}' is not available. You need to enter a new username")
    # if that username does not exist in the current_users list
    else:
        # print "The username is available."
        print(f"The username '{new_user}' is available.")

## H/W : 5-8, 5-9, 5-11

listby5 = []
listby3 = []
listby35 = []

for number in range(1, 101):
    if number % 3 == 0:
        listby3.append(number)
    elif number % 5 == 0:
        listby5.append(number)

for num in listby3:
    if num % 5 == 0:
        listby35.append(num)
print(listby35)

print("###################### 5-9 ######################")
print("###################### Multiplication table ######################")
nums1 = range(1, 11)
nums2 = range(1, 11)
for row in nums1:
    # print(number)
    for col in nums2:
        print(f'{col}*{row} = {row*col}'.ljust(11), end='\t')
    print()
print("######################## option 2 ###################")
nums1 = range(1,11)
nums2 = range(1,11)
for row in nums1:
    for col in nums2:
        print(f"\t{col}*{row}={row*col}", end='\t')
    print()


