# Chapter 9 (cont.)
# Working with Classes and Instances
# Defining the classes here


# create a car class with following state and behav.
# make, model, year,
# mileage (with default) argument/attributes
# implement the logic for mileage:
# 1. should not be visible to user(object), so object can not set the value
# 2. create a function to set_mileage() only when new mileage is greater than previous value and not negative

# get_description(), get_mileage(), set_mileage(new_mileage)
# create a function : increment_odometer(miles)

class Car:
    """General model for all cars."""

    def __init__(self, make: str, model: str, year: int):
        """constructor of Car class."""
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0  # encapsulation: hiding data, it is private
        # java example of the same encapsulation
        # public String make = make;
        # private Int mileage = 0;

    def get_description(self):
        """prints detailed description of the car."""
        print(f"This is {self.make.title()} {self.model.title()} {self.year}.")

    def get_mileage(self):
        """print the odometer reader mileage."""
        print(f"Car has {self.__mileage} miles on it")

    def set_mileage(self, new_mileage):
        """Updates the value of odometer reader."""
        if new_mileage > self.__mileage:
            self.__mileage = new_mileage
            print("odometer reader updated.")
        else:
            print("odometer reader was not updated.")

    def increment_odometer(self, miles):
        if miles > 0:
            # self.__mileage = self.__mileage + miles
            self.__mileage += miles
            print("miles added")
        else:
            print("odometer can not be updated with given value.")

    def fill_gas_tank(self):
        print(f"filling the tank for {self.model} .... Done!")


class ElectricCar(Car):  # inheritance happens here
    """Model for electric cars based on regular car features. Car is parent class."""

    def __init__(self, make, model, year):
        # everything from parent
        super().__init__(make, model, year)  # calling the constructor from parent class
        self.battery_size = 70  # 70kWh

    def fill_gas_tank(self):
        """Polymorphism: Method overriding - overrides the same method from parent class"""
        print(f"This is {self.model}, gas is not used.")

    # not good in python, in java it is called method overloading
    # def fill_gas_tank(self, battery):
    #     """Polymorphism: Method overloading - overrides the same method from parent class"""
    #     print(f"This is {self.model}, gas is not used.")

