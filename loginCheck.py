from template import User
from createUser import createUser

def logincheck(userLog):
    uid = input("id(for new users, type 'register'): ")
    if (uid == ""):
        print("creating a new user")
        uid = createUser()
        print('welcome, ' + uid + '!')
        return(userLog[uid])
    else:
        user = userLog['uid']
        pwd = input("password for " + uid + " :")
        while(user.pwdcheck(pwd) == False):
            print("password is incorrect, please try again")
            pwd = input("password for " + uid + " :")
        print('welcome, ' + uid + '!')
        return(user)