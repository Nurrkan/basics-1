"""
Chapter 10

Files we might deal with as qa engineer

- yaml (similar to dictionaries)
- csv
- text (fixed width)
- xml
- json

Opening in Python:
open('C:/dev/basics/data/somefile) as alias_name:
    # some code to do with file
    # read line by line
    alias_name.exit() or close the file

with open('C:/dev/basics/data/somefile) as alias_name:
    # some code to do with file
    # read line by line
    # it will close the file and clean the memory

windows C:\dev\basics\data\
linux/mac C:\\dev\\basics\\data\\

windows C:/dev/basics/data/
linux/mac C:/dev/basics/data/
"""
# import yaml   # specific library to handle yaml files
from yaml import *  # specific library to handle yaml files


def read_file_1(filepath):
    with open(filepath) as names:
        # print(names)  # returns the object of the file  (reference from the memory)
        # print(names.read())  # returns the body of the file
        print(names.readline())  # reads the current line
        print(names.readline())  # reads the next line
        print(names.readlines())  # creates the list from the rest of the lines
        print(names.name)  # returns the name of the file


def read_file_lines(filepath):
    # with open(filepath) as data:
    #     for line in data.readlines():
    #         print('line value: ', line, end="")
    try:
        print("reading the file...")
        with open(filepath, mode='r') as data:
            for line in data.readlines():
                print('line value: ', line, end="")
        print("\nwoow i have read file ;) ")
        print(f"division for fun: {5 / 0}")
    except (FileNotFoundError) as err:
        print(f"Please check your file path.\n{err}")
    except ZeroDivisionError as err:
        print(f"OOHHH come on man, simple math. {err}")
    finally:
        print("\n\tRead_file_lines functions completed!")


def load_yml(filepath):
    with open(filepath) as data:
        doc = safe_load(data)
    return doc


"""
try:
    # regular code to execute
except SpecificErrorType as aliasNameForErrorMsg:
    # way to handle if above Error happens
except SpecificErrorType1 as aliasNameForErrorMsg:
    # way to handle if above Error happens
except SpecificErrorType2 as aliasNameForErrorMsg:
    # way to handle if above Error happens
except (ErrorType3, ErrorType4) as aliasNameForErrorMsg:
    # way to handle if above Error happens

"""
myfile = "../data/names.txt"
students_path = "../data/students.yml"

# read_file_1(myfile)
# read_file_lines(myfile)
doc = load_yml(students_path)
web_url = doc['credentials'] ['url']
uname = doc['credentials'] ['username']
pword = doc['credentials'] ['password']

bird1 = doc['student1']['calling-birds'][0]
all_birds = doc['student1']['calling-birds']

print('trying to get the url: ', web_url)
print('trying to get the username: ', uname)
print('trying to get the password: ', pword)
print('first bird in the list: ', bird1)
print('list of calling birds: ', all_birds)

print("########### Completed! #################")
