#!/usr/bin/env python3.8

import random
from user import User
from credentials import Credential
from passwordGen import *


def createUser(userName, password):
    newUser = User(userName, password)
    return newUser


def saveUser(user):
    user.saveUser()


# def deleteUser(user):
#     user.deleteUser

def createCredentials(account, userName, password):

    newCredential = Credential(account, userName, password)
    return newCredential


def saveCredentials(credential):
    credential.saveCredentials()


def displayCredentials():
    return Credential.displayCredentials()

def deleteCredentials(account):
    return Credential.deleteCredentials(account)


def main():
    print('Welcome to password locker.')

    while True:
        print('\n')
        print('**********')
        print('Use these short codes to navigate : cu - create a new user, lg - login to your account, ex -exit the password locker')
        print('**********')

        shortCode = input().lower()

        if shortCode == 'cu':
            print('----------')
            print('Create account...')
            print('----------')
            print('Enter username: ')
            createdUserName = input()
            print('…')

            passResponse = input(
                'Do you want a generated password? \n  Respond with \'y\' for yes or \'n\' for no: ').lower()

            if passResponse == 'y':
                createdPass = passwordGenerator(getPassLength())
                confirmedPass = createdPass

                print(
                    f'New password ({str(len(createdPass))}): -----> {createdPass}')
            else:
                print('Enter password: ')
                createdPass = input()

                print('Comfirm password: ')
                confirmedPass = input()

            print('\n')

            if createdPass != confirmedPass:
                print('Invalid: Passwords did not match!')
                print('Enter password: ')
                createdPass = input()

                print('Confirm password: ')
                confirmedPass = input()
            else:
                saveUser(createUser(createdUserName, createdPass))

                print(
                    f'Congratulations {createdUserName}, your account creation was successful!')
                print('----------')
                print('Proceed to login...')
                print('----------')
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
                print('\n')
                print(f'{enteredUsername} welcome to your account.')
                print('\n')

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

                while True:
                    print('\n ………')
                    print(
                        'Use these short codes to navigate through credentials : ac - add credential, lc - list credentials, dc - delete credential, ex - exit')
                    print('………')

                    credetialCode = input().lower()
                    if credetialCode == 'ac':
                        print('----------')
                        print('Save new credential...')
                        print('----------')
                        print('Enter account to save credentials for: ')
                        credAccount = input()
                        print('…')

                        print('Enter username: ')
                        credUserName = input()
                        print('…')

                        passResponse = input(
                            'Do you want a generated password? \n  Respond with \'y\' for yes or \'n\' for no: ').lower()

                        if passResponse == 'y':
                            createdPass = passwordGenerator(getPassLength())
                            confirmedPass = createdPass

                            saveCredentials(createCredentials(
                                credAccount, credUserName, createdPass))
                            print(
                                f'New password ({str(len(createdPass))}): -----> {createdPass}')
                        else:
                            print('Enter password: ')
                            credPass = input()

                            print('Comfirm password: ')
                            confirmedPass = input()

                            print('\n')

                            if credPass != confirmedPass:
                                print('Invalid: Passwords did not match!')
                                print('Enter password: ')
                                credPass = input()

                                print('Confirm password: ')
                                confirmedPass = input()
                            else:
                                saveCredentials(createCredentials(
                                    credAccount, credUserName, credPass))
                                print(
                                    f'Congratulations your credentials for {credAccount} was successfully created!')
                                print('\n')

                    # source of error have a look
                    #
                    elif credetialCode == 'lc':
                        if displayCredentials():
                            print('Here is a list of all your contacts')
                            print('\n')

                            for credential in displayCredentials():
                                print(
                                    f'{credential.account}: \nuser name: {credential.username}, password: {credential.password}')

                            print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')
                    elif credetialCode == 'dc':
                        account = input('Enter account you no longer want to store credentials for: ')
                        deleteCredentials(account)
                            
                    elif credetialCode == 'ex':
                        break

                    else:
                        print('Invalid credentials short code')
                else:
                    break

        elif shortCode == 'ex':
            break

        else:
            print('Invalid short code')


if __name__ == '__main__':

    main()
