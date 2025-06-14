allUsers = {}
global currentUser
currentUser = None

def signUp(userName, password):
  if userName in allUsers:
    return False
  allUsers[userName] = User(password)
  return True
def signIn(userName, password):
  global currentUser    
  if allUsers[userName].password == password:
    currentUser = allUsers[userName]
    return True
  return False
def signOut():
  global currentUser
  currentUser = None

def createNewAccount(accountName, sum):
  currentUser.accounts[accountName] = sum
def checkAccount(accountName):
  return currentUser.accounts[accountName]
def deposit(accountName, sum):
  currentUser.accounts[accountName] += sum
def withdraw(accountName, sum):
  if currentUser.accounts[accountName] < sum:
    return False
  currentUser.accounts[accountName] -= sum
  return True
def Transfer(accountFrom, accountTo, sum):
  if currentUser.accounts[accountFrom] < sum:
    return False
  currentUser.accounts[accountFrom] -= sum
  currentUser.accounts[accountTo] += sum

class User:
  def __init__(self, password):
    self.password = password
    self.accounts = {}


class Account:
  def __init__(self, accountName, sum):
    self.accountName = accountName
    self.sum = sum
