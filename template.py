
class Booking:
    def __init__(self, uid, room, date, time, duration):
        self.uid = uid
        self.room = room
        self.date = date
        self.time = time
        self.duration = duration

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
