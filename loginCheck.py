from template import User
from createUser import createUser

def loginCheck(userLog):
    uid = input("id(for new users, type 'register'): ")
    if uid == 'register':
        print("creating a new user")
        userLog = createUser(userLog)
        return userLog
    elif uid in userLog:
        user = userLog[uid]
        pwd = input("password for " + uid + " :")
        while(user.pwdCheck(pwd) == False):
            print("password is incorrect, please try again")
            pwd = input("password for " + uid + " :")
        print('welcome, ' + uid + '!')
        return userLog
    else:
        print('user not found, please try again')
        return loginCheck(userLog)
