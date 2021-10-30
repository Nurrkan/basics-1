# execution of Dog class, using objects
# from dogs import *
from classes.dogs import Dog, Cat

dog1 = Dog('krish', 'white', 'American Eskimo', 6)  # instantiation
# __init__ functions is automatically called (executed)
# dog1 - object; instance of Dog class
# 'krish', 'white', 'American Eskimo', 6 - instance variables

print("####### accessing the variables of the object based on the model ########### ")
print('name of the dog: ', dog1.name)
print('color of the dog: ', dog1.color)
print('age of the dog: ', dog1.age)
print('breed of the dog: ', dog1.breed)

print("######### accessing the methods(functions) DOG1 ###############")
dog1.run()
dog1.bark()
dog1.sit()
dog1.description()
dog1.age = 8
dog1.description()

dog2 = Dog(age=6, breed='French Bulldog', color='black', name='Avni')
dog3 = Dog('jak', 'brown', 'boerboel', 7)

print("######### accessing DOG2 ###############")
dog2.run()
dog2.bark()
dog2.sit()
dog2.description()

print("######### accessing DOG3 ###############")
dog3.run()
dog3.bark()
dog3.sit()
dog3.description()

"""
Selenium samples:
ok_button = 'asdfadfasdf'
text_box = '//asdfasdf/asdfasd/asdf'

text_box.send_keys('python selenium')
ok_button.click()
"""
cat1 = Cat()

print("################# 9-1 ########################")


class Restaurant():
    # restaurant_name, cuisine_type
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # describe_restaurant() - use 2 variables above
    def describe_restaurant(self):
        print(f"We are '{self.restaurant_name.title()}' and we are {self.cuisine_type.upper()} restaurant.")

    # open_restaurant() - print("we are open")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")


restaurant = Restaurant('taco bells', 'mexican')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.cuisine_type = 'american-mexican'
print('after updating the cuisine type: ', restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()

# H/W : 9-2, 9-3
