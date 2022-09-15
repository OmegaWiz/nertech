from template import User

def createUser(userLog):
    uid = input('enter new id:')
    while uid in userLog:
        print('user already exists, please enter new id')
        uid = input('enter new id:')
    pwd = input('enter new password:')
    rank = int(input("role(1: student, 5: teacher):"))
    userLog[uid] = User(uid, pwd, rank)
    print('welcome, ' + uid + '!\n')
    return (userLog[uid], userLog)