from asyncio.windows_events import NULL
from template import User
from createUser import createUser

def loginCheck(userLog):
    uid = input("id:")
    user = NULL
    for i in userLog:
        if i.getId() == uid:
            user = i
            break
    if user:
        pwd = input("password for " + uid + ":")
        while(user.pwdCheck(pwd) == False):
            print("password is incorrect, please try again")
            pwd = input("password for " + uid + ":")
        print('welcome, ' + uid + '!')
        return (user, userLog)
    else:
        print('user not found, please try again')
        return loginCheck(userLog)