class User:
    '''
    class to generate an instance of a new user
    '''

    userList = []

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def saveUser(self):
        User.userList.append(self)

    def delteUser(self):
        User.userList.remove(self)
