
class Booking:
    import datetime
    def __init__(self, user='user', room='room', beginTime=datetime.datetime.now(), endTime=datetime.datetime.now()):
        self.user = user
        self.room = room
        self.beginTime = beginTime
        self.endTime = endTime
        self.status = "booked"
        self.desc = ""

    def overrideBooking(self, user):
        if user.printRank() > self.user.printRank():
            self.status = 0
            return 1
        else:
            return 0
    
    def printBooking(self):
        print("booking for {self.user}\nroom: {self.room}\ntime: {self.beginTime} - {self.endTime}\nstatus: {self.status}\ndescription: {self.description}")
    
    def getStatus(self):
        return self.status

    def getTime(self):
        return (self.beginTime, self.endTime)

    def getUser(self):
        return self.user
    
    def getRoom(self):
        return self.room

    def getDesc(self):
        return self.desc

class User:
    def __init__(self, uid='user', pwd='user', rank=1):
        self.uid = uid
        self.pwd = pwd
        self.rank = rank
        
    def getId(self):
        return uid

    def getRank(self):
        return self.rank

    def pwdCheck(self, pwd):
        if(self.pwd == pwd):
            return True
        else:
            return False

class BookingList:
    def __init__(self):
        self.list = [Booking()]
    
    def sortBooking(self):
        self.list.sort(key=getTime())

    def nextBooking(self):
        pass

    def incomingBooking(self):
        pass

    def myNextBooking(self, user=User()):
        pass

    def myIncomingBooking(self, user=User()):
        pass

    def addBooking(self, booking=Booking()):
        #add booking to the list and sort
        pass

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
