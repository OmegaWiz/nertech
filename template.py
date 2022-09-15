
class Booking:
    def __init__(self, user, room, date, time, duration):
        self.user = user
        self.room = room
        self.date = date
        self.time = time
        self.duration = duration
        self.status = 1

    def override(self, user):
        if user.rank > self.user.rank:
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
