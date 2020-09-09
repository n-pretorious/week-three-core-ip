class Credential:
  '''
  class to generate an instance of a user's credential(s)
  '''

  credentialList = []

  def __init__(self, account, username, password):
    self.account = account
    self.username = username
    self.password = password

  def saveCredentials(self):
    Credential.credentialList.append(self)

  @classmethod
  def deleteCredentials(cls, account):
    for credential in cls.credentialList:
      if credential.account == account:
        cls.credentialList.remove(credential)

  @classmethod
  def displayCredentials(cls):
    return cls.credentialList
