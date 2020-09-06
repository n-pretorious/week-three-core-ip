#!/usr/bin/env python3.8

import random
from user import User

def createUser(userName, password):
    newUser = User(userName, password)
    return newUser


def saveUser(user):
    user.saveUser


def deleteUser(user):
  user.deleteUser


def main():
    print('Welcome to password locker \n')

    while True:
        print('Use these short codes to navigate : cu - create a new user, lg - login to your account, ex -exit the password locker \n')

        shortCode = input().lower()
        print('\n')

        if shortCode == 'cu':
            print('Create username: ')
            createdUserName = input()

            print('Create password: ')
            createdPass = input()

            print('Comfirm password: ')
            comfirmemPass = input()

            if createdPass != comfirmemPass:
                print('Invalid: Passwords did not match!')
                print('Enter password: ')
                createdPass = input()

                print('Confirm password: ')
                comfirmemPass = input()
            else:
                print(
                    f'Congratulations {createdUserName}, your account creation was successful! \n')
                print('Proceed to login')
                print('Enter your username: ')
                enteredUsername = input()

                print('Enter password: ')
                enteredPassword = input()

            if enteredUsername != createdUserName and enteredPassword != createdPass:
                print('Invalid username or password')
                print('Enter username: ')
                enteredUsername = input()

                print('Enter password: ')
                enteredPassword = input()
            else:
                print(f'{enteredUsername} welcome to your account.')

        elif shortCode == 'lg':
            print('Enter your username: ')
            defaultUserName = input()

            print('Enter password: ')
            defaultPassword = input()
            print('\n')

            if defaultUserName != 'test' or defaultPassword != '1234':
                print(
                    'Wrong username and password. Default username is: \'test\' and password is: \'1234\' ')
                print('Enter username: ')
                defaultUserName = input()

                print('Enter password: ')
                defaultPassword = input()

            else:
                print('Login success! \n')
                print('\n')

        elif shortCode == 'ex':
          break
        
        else:
          print('Invalid short code')

if __name__ == '__main__':

    main()
