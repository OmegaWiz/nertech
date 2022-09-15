'''
DESCRIPTION
check if requested booking time duration is
    available,
    overridable, or 
    unavailable

RETURN VALUE
return either "available, "overridable", or "unavailable" 
''' 

import datetime
from template import Booking, User

def checkBooking(   user=User(), 
                    bookingLog=[Booking()],
                    startTime=datetime.datetime.now(), 
                    endTime=datetime.datetime.now() + datetime.timedelta(hours=1)):
    '''
    bookedTime = input("please enter the time you would like to book (for example, 20:10)")
        l = bookedTime.split(':')
        bookedTime = datetime.time(hour=int(l[0]), minute=int(l[1]))
        startTime = datetime.datetime.combine(datetime.date.today, bookedTime)
        while startTime < datetime.datetime.now():
            print("the selected time is unavailable, please try again")
            bookedTime = input("please enter the time you would like to book (for example, 20:10)")
            l = bookedTime.split(':')
            bookedTime = datetime.time(hour=int(l[0]), minute=int(l[1]))
            startTime = datetime.datetime.combine(datetime.date.today, bookedTime)
        duration = int(input("please enter the number of hour(s) you would like to book:"))
        while duration < 1 or duration > 10:
            print("the number of hours you're trying to book is unavailable, please try again")
            duration = int(input("please enter the number of hour(s) you would like to book:"))
        endTime = startTime + datetime.timedelta(hours=duration)
        isSucessful = True
        for i in bookingLog:
            if i.room == room:
                if (i.startTime < startTime and startTime < i.endTime) or (i.startTime < endTime and endTime < i.endTime)):
                    isSucessful = False
                    break
        if isSucessful:
            print("booking successful")
            return bookingLog
        print('the requested hour(s) are unavailable, please try again')
    '''
    return "AVAILABLE"