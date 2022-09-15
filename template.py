
class Booking:
    def __init__(self, user, room, beginTime, endTime):
        self.user = user
        self.room = room
        self.beginTime = beginTime
        self.endTime = endTime
        self.status = 1

    def override(self, user):
        if user.printRank() > self.user.printRank():
            self.status = 0
            return 1
        else:
            return 0

    '''
    status
    1 - booked
    0 - canceled
    2 - successful
    '''

class User:
    def __init__(self, uid, pwd, rank):
        self.uid = uid
        self.pwd = pwd
        self.rank = rank

    def pwdCheck(self, pwd):
        if(self.pwd == pwd):
            return True
        else:
            return False
            
    def printRank(self):
        return self.rank
