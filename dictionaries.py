# new line to test git from akmal branch

# data structure - to handle complex data
# key: value, all keys are unique
# dictName = {}
# dictName = { 'key1': 'value1', 'key2': 'value2', 'key3': 'value3' }

student1 = {'name': 'Steven',
            'age': 25,
            'city': 'Brooklyn'}
student1_list = ['Steven', 25, 'Brooklyn']
print('what is this', student1)
print(type(student1))
print(type(student1_list))

# Accessing the dictionary
print('from the list: ', student1_list[0])
print('from the dictionary: ', student1['name'])
print(student1)

# adding the elements to the dictionary
student1['country'] = 'USA'
print(student1)
print(sorted(student1))  # returns sorted list of keys, temp list

# Removing the duplicates from the list
nums = [3, 4, 6, 3, 2, 0, 2, 0, 1, 1, 1, 1, 5]
# nums_set = set(nums)
# print(nums_set)
u_nums = list(set(nums))
print(nums)
print(u_nums)

print("#################### sets in python (vs in SQL) ###########")
'''
# SQL: customers, city ;  suppliers, city
# get the cities where you have customers and suppliers
select city from customers
intersect
select city from suppliers

# cities with only customers
select city from customers
except
select city from suppliers
'''

set1 = {3, 4, 5, 6, 7, 8, 9}
set2 = {7, 8, 9, 10, 11, 12}
print('union: ', set1.union(set2))
print('intersection: ', set1.intersection(set2))
print('difference set1 from set2: ', set1.difference(set2))
print('difference set2 from set1: ', set2.difference(set1))

print("\n###### Modifying the values in the dictionary ########")
student1['ages'] = 26  # make sure you use existing key when you are updating the value
student1['age'] = 27
print(student1)

# student1['age'] = student1['age'] + 2
student1['age'] += 2
print(student1)

# Removing the key-value pair from the dictionary
del student1['ages']
print(student1)

print("\n# Looping the dictionaries")

print("############ by default (based on keys) ##################")
for key in student1:  # dictionary by default returns list of keys here
    print('key:', key)
    print('values using the keys:', student1[key])

print("################ by keys ########################")
for key in student1.keys():  # keys() function is creating temp list of keys
    print('key:', key)
    print('values using the keys:', student1[key])
print("############ to have guaranteed order of keys #############")
for key in sorted(student1.keys()):  # keys() function is creating temp list of keys
    print('key:', key)
    print('values using the keys:', student1[key])

print("################ by values ########################")
for value in student1.values():  # values() function is creating temp list of values
    print('value of the dict:', value)

print("################# by keys, values ######################")
for key, value in student1.items():  # items() function is creating temp list of keys, values
    print('key of the dict, this is the output1 from items():', key)
    print('value of the key, this is the output2 from items():', value)

# hw: 6-1 , 6-2, 6-3
# hw: 6-4 , 6-5, 6-6
