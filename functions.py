# Chapter 8 : Functions (java, c# - method)

# declaring, defining function here
def greet_user():
    """
    Function to say hello. this is docstring where you describe your function.
    """
    print("Hello!")
    """
    regular multi line comment 
    """
    print("Welcome to the class!")


def greet_user_name(user_name):
    # user_name = 'john'
    print(f"Helloooo, {user_name.title()}!")


def greet_user_input():
    user_name = input("enter your username: ")
    print(f"Helloooo, {user_name.title()}!")


def exercise_6_6():
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


def greet_user1(fname, lname, mid_name=""):
    print(f"Hi, {fname.title()} {mid_name.title()}!\n\t Mr./Mrs {lname.title()} please take your seat.")


def get_largest_number(nums_list: list) -> int:
    """
    prints largest number in the list
    :param nums_list: this should be list of number
    :return:
    """
    # print('the largest number is :', max(nums_list))
    # print('this is it')
    return max(nums_list)


def describe_city(city, country="united states of america"):
    print(f"{city.title()} is in {country.title()}.")


def make_album(artist_name, album_title, num_tracks=None):
    """

    :param artist_name: required positional arguments
    :param album_title: required positional arguments
    :param num_tracks: keyword argument
    :return:
    """
    album = {'Artist': artist_name,
             'album': album_title,
             'tracks': num_tracks}
    return album


# calling the function, actual execution happens
def functions1():
    greet_user()
    greet_user()
    # greet_user("john") # TypeError: greet_user() takes 0 positional arguments but 1 was given
    # greet_user_name() # TypeError: greet_user_name() missing 1 required positional argument: 'user_name'
    greet_user_name('john')
    greet_user_name('nilufar')
    greet_user_name('irene')
    # greet_user_input()
    exercise_6_6()


# hw: 8-9, 8-10, 8-11
# hw: Palindrome, create a functions that tell if the word is palindrome or not
# return True if palindrome False if it is not palindrome
# you might need for loop and if condition
def is_palindrome(word):
    result = None
    return result
