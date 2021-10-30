## Exercises in Chapter 4:

print("######### 4.5 ################")
print("# create a list of numbers from 1 to 1000000")
# for num in range(1, 100001):
#     print(num)
nums = list(range(1, 1000001))
print(f"min: {min(nums)}")
print(f"max: {max(nums)}")
print(f"sum: {sum(nums)}")

print("#################### 4-7 ##################")
multiplesOf3 = []
for number in range(3, 31, 3):
    multiplesOf3.append(number)
print(multiplesOf3)

print("#################### 4-8 ##################")
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
print(cubes)

print("#################### 4-9 ##################")
cubes2 = [num ** 3 for num in range(1, 11)]
print(cubes2)

print("#################### 4-11 ##################")
pizzas = ['grandma', 'margarita', 'chicken']
friend_pizzas = pizzas[:]
print(pizzas)
print(friend_pizzas)
pizzas.append('mushroom')
friend_pizzas.append('stake')
print(pizzas)
print(friend_pizzas)
print('my favourite pizzas are')
for pizza in pizzas:
    print(pizza)
print("my friend's favourite pizzas are")
for pizza in friend_pizzas:
    print(pizza)
