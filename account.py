allUsers = {}
currentUser = None
def signUp(userName, password):
  if userName in allUsers:
    return False
  allUsers[userName] = password
  return True
def signIn(userName, password):
  if allUsers[userName] == password:
    currentUser = userName
    return True
  return False
def signOut():
  currentUser = None