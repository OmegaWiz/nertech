'''
RETURN VALUE
the available time slot
'''
import datetime
from template import Booking, BookingList

def timeCut(i=(datetime.datetime(), datetime.datetime()), j=(datetime.datetime(), datetime.datetime())):
    if j[0] < i[0]:
        i[0] = j[1]
    if j[1] > i[1]:
        i[1] = j[0]
    return i
    
def timeSplit(i=(datetime.datetime(), datetime.datetime()), j=(datetime.datetime(), datetime.datetime())):
    x = (i[0], j[0])
    y = (j[1], i[1])
    return [x, y]

def timeSubtract(i=(datetime.datetime(), datetime.datetime()), j=(datetime.datetime(), datetime.datetime())):
    if j[0] <= i[0] or j[1] >= i[1]:
        return None
    if j[0] < i[0] or j[1] > i[1]:
        return timeCut(i, j)
    else:
        return timeSplit(i, j)

def checkBooking(timeList=[(datetime.datetime(), datetime.datetime())], bookingLog=BookingList()):
    newTimeList = []
    for i in timeList:
        for j in bookingLog:
            if i[0] < j[1] and j[1] < i[1]:
                i = timeSubtract(i, j)
            elif i[0] < j[0] and j[0] < i[1]:
                i = timeSubtract(i, j)
        newTimeList.append(i)
    return newTimeList