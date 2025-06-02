allUsers = {}
currentUser = None

def signUp(userName, password):
  if userName in allUsers:
    return False
  allUsers[userName] = User(password)
  return True
def signIn(userName, password):
  if allUsers[userName].password == password:
    currentUser = userName
  return False
def signOut():
  currentUser = None

def createNewAccount(accountName, sum):
  currentUser.accounts[accountName] = sum
def checkAccount(accountName):
  return currentUser.accounts[accountName]


class User:
  def __init__(self, password):
    self.password = password
    accounts = {}


class Account:
  def __init__(self, accountName, sum):
    self.accountName = accountName
    self.sum = sum
