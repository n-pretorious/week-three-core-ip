import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.newUser = User('test', '0000')

    def testInit(self):
        self.assertEqual(self.newUser.userName, 'test')
        self.assertEqual(self.newUser.password, '0000')

    def testSaveUser(self):
        self.newUser.saveUser()
        testUser = User('test2', '1111')

        testUser.saveUser()
        self.assertEqual(len(User.userList), 2)

    def tearDown(self):
        User.userList = []

    def testSaveMultipleUsers(self):

        self.newUser.saveUser()
        self.assertEqual(len(User.userList), 1)

    def testDeleteUser(self):
        self.newUser.saveUser()
        testUser = User('test2', '1111')
        testUser.saveUser()

        self.newUser.delteUser()
        self.assertEqual(len(User.userList), 1)


if __name__ == '__main__':
    unittest.main()
