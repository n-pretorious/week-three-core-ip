import string
import random


def getPassLength():
    '''
    Retrieves the length of a password
    :returns number <class 'int'>
    '''
    length = input("Length of your password: ")
    return int(length)


def passwordGenerator(length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified.
    :returns string <class 'str'>
    '''

    password = list(string.ascii_letters + string.punctuation + string.digits)
    random.shuffle(password)
    random_password = ''.join(random.choices(password, k=length))

    return random_password
