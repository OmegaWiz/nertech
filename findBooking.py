'''
DESCRIPTION
receives the input of the details of the booking from user and returns the most matching one

RETURN VALUE
return the matching booking
''' 

from datetime import datetime
from importBooking import importBooking
from template import Booking, User, BookingList
from importBooking import importBooking

def findBooking(user=User(), bookingLog=importBooking()):
    yn = 'n'
    while yn == 'n':
        bookingId = input("type the id of the booking you would like to find:")
        room = None
        for i in bookingLog:
            if bookingId in i:
                room = i.getName()
                break
        if room in bookingLog:
            break
        else:
            yn = input("no such booking exist, would you like to use other information to find (y/n): ")
    if yn == 'n':
        yn = 'y'
    else:
        yn = 'n'
    while yn == 'n':
        room = input("which room is the booking at:")
        while not (room in bookingLog):
            print("no such room exist, try again")
            room = input("which room is the booking at:")
        while yn =='n':
            beginTime = input("when does your booking begin (your format must be YYYY-MM-DDTHH:MM:DD):")
            for i in bookingLog[room].getList():
                if i.getBeginTime() == datetime.fromisoformat(beginTime):
                    bookingId = i.getBookingId()
                    booking = i
                    yn = 'y'
                    break
            if yn == 'n':
                print("no such booking exist")
        i.printBooking()
        yn = input("is this your booking (y/n):")
    return (room, bookingId)