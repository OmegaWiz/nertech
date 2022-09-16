from template import User
from createUser import createUser

def loginCheck(userLog):
    '''''
    uid = input("id(for new users, type 'register'): ")
    if uid == 'register':
        print("creating a new user")
        (user, userLog) = createUser(userLog)
        return (user, userLog)
    elif uid in userLog:
        user = userLog[uid]
        pwd = input("password for " + uid + " :")
        while(user.pwdCheck(pwd) == False):
            print("password is incorrect, please try again")
            pwd = input("password for " + uid + " :")
        print('welcome, ' + uid + '!')
        return (user, userLog)
    else:
        print('user not found, please try again')
        return loginCheck(userLog)
    '''''
    uid = input("id: ")
    if uid in userLog:
        user = userLog[uid]
        pwd = input("password for " + uid + " :")
        while(user.pwdCheck(pwd) == False):
            print("password is incorrect, please try again")
            pwd = input("password for " + uid + " :")
        print('welcome, ' + uid + '!')
        return (user, userLog)
    else:
        print('user not found, please try again')
        return loginCheck(userLog)