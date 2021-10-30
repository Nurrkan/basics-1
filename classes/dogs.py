"""
Chapter 9
Object-oriented programming - modeling the real world object and using them in program
Class - model of something; generic state(description) and behavior of object(car, dog, tree, human, etc..)
object - instance of class; one of the sample of model;
instantiation - creating an object from class
self - keyword that shows variable and functions belongs to current class (in java 'this' keyword)
- how to call functions from the model using the object
- how to update/access variables from the class (attributes)
- what is constructor? in python it is __init__() method

"""
HOME = 'C:/dev/basics'


class Dog():
    """
    This is the model for generic dog.
    """

    # state/property/instance variable: name, color, breed, age, number_of_leg = 4
    def __init__(self, name, color, breed, age):
        """Constructor: Initialize variables name, color, breed, age."""
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.number_of_leg = 4

    # behavior: run(), sit(), bark()
    def run(self):
        print(f"{self.name.title()} is running with {self.number_of_leg} legs ....")

    def sit(self):
        print(f"{self.name.title()} is sitting :) ")

    def bark(self):
        print(f"{self.name.title()}is barking: woof woof!!!!!!!")

    def description(self):
        print(
            f"Hi this is {self.name}, I am a beautiful {self.color} colored dog. I am {self.age} years old and I am a '{self.breed}'")


class Cat():
    def __init__(self):
        # in this case constructor is optional since python creates automatically
        pass  # do nothing in python

    def sit(self):
        print("cats dont like to sit so I will lay down.")
