# module is a python file
from functions import *
from functions import greet_user1 as gu1  # using alias name
from test.more_functions import *


gu1(lname='jackson', fname='michael')
gu1('john', 'travolta')

nums = [45, 3, 4, 56, 441, 78, -456]
get_largest_number(nums)

# chars = ['aa','b', 'z', True]
# get_largest_number(chars)

# HW: Exercise 8.3, 8.4
print("############### Exercise 8.5 #############")

describe_city('new york')
describe_city('paris', 'france')

print("########## return statement ###################")
nums = [45, 3, 4, 56, 441, 78, -456]
result = get_largest_number(nums) + 1000
print('result of the function: ', result)

chars = ['aa', 'b', 'z', 'bbc']
print(get_largest_number(chars))

print("########## 8-7: Album ###################")
album1 = make_album("Arcade Fire", 'Funeral')
album2 = make_album("Shakira", 'Dónde Están los Ladrones')
album3 = make_album("The Beatles", 'White Album', 30)

print(album1, album2, album3)
print(f"{album1['Artist']} had a great album named {album1['album']}")
print(f"{album2['Artist']} had a great album named {album2['album']}")
print(f"{album3['Artist']} had a great album named {album3['album']} with {album3['tracks']} tracks on it.")

print("############### importing with packages ##########")
get_temp_today()