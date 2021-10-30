# Chapter 6: h/W Exercises
# hw: 6-1 , 6-2, 6-3
# hw: 6-4 , 6-5, 6-6
print("########## 6-1 ######################")
freind1 = {'first_name': 'Shahlo', 'last_name': 'Alieva', 'age': 25,
           'city': 'Tashkent'}
print(freind1['first_name'], freind1['last_name'], freind1['age'], freind1['city'])

freind2 = {'first_name': 'Nazokat', 'last_name': 'Ahrarova', 'age': 23,
           'city': 'Brooklyn'}
friends = [freind1, freind2]
print(friends)
print(friends[0]['first_name'])
print(freind1['first_name'])
print(friends[1]['first_name'])

print("########## 6-2 ######################")
fav_numbers = {
    'nilufar': 2,
    'alex': 9,
    'dorin': 6,
    'maftuna': 7
}
for name, num in fav_numbers.items():
    print(f"{name.title()}'s favourite number is '{num}'.")
    # print(x.title() + "'s favorite number is", y)
# print("Silvia's favorite number is " + str(favorite_numbers['Silvia']) + ".")

# num = favorite_numbers ['nilfura']
# Pirnt (nilfura fovire number is " + str(numb) + ".")

print("########## 6-3, 6-4 ######################")
glossary = {
    'variable': 'reference that can store a data',
    'string': 'A sequence of characters',
    'list': 'A collection of elements in a particular order',
    'loop': 'An  iteration over an object until that object is complete',
    'dictionary': "A collection of key-value pairs",
}
for word, definition in glossary.items():
    print("\n" + word.upper() + ": \n\t" + definition)

print("########## 6-5: Rivers ######################")
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
    'ganga': 'india'
}
print("### sentences using river name and country ####")
for river, country in rivers.items():
    if country == 'usa':
        print(f"The {river.title()} runs through {country.upper()}.")
    else:
        print(f"The {river.title()} runs through {country.title()}.")

print("### list the names of rivers ####")
rivers_list = []
for river in rivers.keys():
    rivers_list.append(river)
print(rivers_list)
print("### list the names of rivers, using list comprehension ####")
rivers_list_comp = [river for river in rivers.keys()]
print(rivers_list_comp)

print("### list the names of countries, using list comprehension ####")
country_list_comp = [country.title() for country in rivers.values()]
print(country_list_comp)

print("########## 6-6: Polling ######################")
fav_lan = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
names = ['jen', 'mark', 'edward', 'john']
for name in names:
    # if 'python' in fav_lan.values(): to check python from values list
    if name in fav_lan:
        print(f"{name.title()}, Thank  you for your vote!")
    else:
        print(f"{name.title()}, Please take a poll about a favourite language.")