# Chapter 9 (cont.)
# Working with Classes and Instances
# Instantiating the classes (executing)
from classes.cars import *

car1 = Car('toyota', 'camry', 2021)
print(car1.make)
print(car1.model)

car1.get_description()
car1.get_mileage()
# print('miles:', car1.__mileage) # it was hidden from object
# car1.mileage = 25    # name before modifying
# car1.__mileage = 25
car1.set_mileage(25)
car1.get_mileage()
# car1.__mileage = -25
car1.set_mileage(-5)
car1.get_mileage()
car1.set_mileage(24)
car1.get_mileage()
print("------------------------------")
car1.increment_odometer(50)
car1.get_mileage()
car1.increment_odometer(-10)  # not possible in real world
car1.get_mileage()

print("------------ Electric Car ------------------")

car2 = ElectricCar('Tesla', 'Model X', 2022)
car2.get_description()
print(car2.model)
car1.fill_gas_tank()
car2.fill_gas_tank()
# car2.fill_gas_tank('abc')
# H/w : https://www.indeed.com/career-advice/career-development/what-is-object-oriented-programming

# Exercises: 9-4, 9-5, 9-6, 9-7, 9-8, 9-9

# Agenda:
# Chapter 10: high level
# Appendix D: Using Git for Version Control
#    prior to class: register to github https://github.com/
    # precise usernames