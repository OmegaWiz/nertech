
from datetime import datetime
from uuid import uuid4

class Booking:
    import datetime
    import uuid
    def __init__(self, user='user', room='room', beginTime=datetime.datetime.now(), endTime=datetime.datetime.now(), bookingId=uuid.uuid4()):
        self.bookingId=bookingId
        self.user = user
        self.room = room
        self.beginTime = beginTime
        self.endTime = endTime
        self.status = "booked"
        self.desc = ""

    def findBooking(self, bookingId):
        if self.bookingId == bookingId:
            return True
        else:
            return False

    def overrideBooking(self, user):
        if user.printRank() > self.user.printRank():
            self.status = 0
            return 1
        else:
            return 0
    
    def printBooking(self):
        print("booking for ",self.user,"\nroom: ",self.room,"\ntime: ",self.beginTime," - ",self.endTime,"\nstatus: ",self.status,"\ndescription: ",self.desc)

    def getBookingId(self):
        return self.bookingId
    
    def getStatus(self):
        return self.status

    def getTime(self):
        return (self.beginTime, self.endTime)

    def getBeginTime(self):
        return self.beginTime

    def getEndTime(self):
        return self.endTime

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
        return self.uid

    def getRank(self):
        return self.rank

    def pwdCheck(self, pwd):
        if(self.pwd == pwd):
            return True
        else:
            return False

    def printUser(self):
        print ("id: ", self.uid,"\npwd: ", self.pwd, "\nrank:", self.rank)


class BookingList:
    def __init__(self, name, list=[Booking()]):
        self.list = list
        self.name = name

    def getName(self):
        return self.name

    def getList(self):
        return self.list
    
    def sortBooking(self):
        self.list.sort(key=getTime())

    def nextBooking(self):
        for i in self.list:
            if i.beginTime > datetime.datetime.now():
                return (i)

    def incomingBooking(self):
        nextBookingList = []
        for i in self.list:
            if i.beginTime > datetime.datetime.now():
                nextBookingList.append(i)
        return nextBookingList

    def myNextBooking(self, user=User()):
        for i in self.list:
            if i.beginTime > datetime.datetime.now() and i.getUser == user:
                return (i)

    def myIncomingBooking(self, user=User()):
        nextBookingList = []
        for i in self.list:
            if i.beginTime > datetime.datetime.now() and i.getUser == user:
                nextBookingList.append(i)
        return nextBookingList

    def addBooking(self, booking=Booking()):
        bookingTime = booking.getBeginTime()
        for i in range(0, len(self.list)):
            selfTime = self.list[i].getBeginTime()
            if selfTime > bookingTime:
                self.list.insert(i, booking)
                break
