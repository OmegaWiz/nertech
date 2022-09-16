from base64 import encode
from fileinput import close
from template import User


def importBooking(fileName="./bookingLog.csv"):
    import csv
    import template
    '''
    userLog = []
    with open(fileName, 'r') as file:
        stdread = csv.reader(file)
        for row in stdread:
            userLog.append(User(uid=row[0], pwd=row[1], rank=row[2]))
            print('user imported: ' + row[0])
    close()
    print(userLog[1].pwd)
    print("successfully import all users")
    return userLog
    '''