import unittest
from credentials import Credential


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.newCredentials = Credential(
            'test1', 'test1@test.com', '0000')

    def testInit(self):
        self.assertEqual(self.newCredentials.account, 'test1')
        self.assertEqual(self.newCredentials.username, 'test1@test.com')
        self.assertEqual(self.newCredentials.password, '0000')

    def testSaveCredentials(self):
        self.newCredentials.saveCredentials()
        testCredentials = Credential('test2', 'test1@test.com', '1111')

        testCredentials.saveCredentials()
        self.assertEqual(len(Credential.credentialList), 2)

    def tearDown(self):
        Credential.credentialList = []

    def testSaveMultipleCredentials(self):
  
        self.newCredentials.saveCredentials()
        self.assertEqual(len(Credential.credentialList), 1)

    def testDeleteCredentials(self):
        self.newCredentials.saveCredentials()
        testCredentials = Credential('test3', 'test3@test.com', '2222')
        testCredentials.saveCredentials()

        self.newCredentials.deleteCredentials('test3')
        self.assertEqual(len(Credential.credentialList), 1)


if __name__ == '__main__':
    unittest.main()
