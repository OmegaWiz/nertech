from template import User
from importUser import importUser

def saveUser(userLog=importUser(), fileName="./userLog.csv"):
    import csv
    with open(fileName, 'w', encoding='UTF8', newline='') as file:
        stdwrite = csv.writer(file)
        for user in userLog:
            stdwrite.writerow([user.getId(), user.getPwd(), user.getRank()])
    print("successfully save all users")