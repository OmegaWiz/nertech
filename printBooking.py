'''
DESCRIPTION
print all, incoming, or next booking of the user

RETURN VALUE
none
'''
from importBooking import importBooking
from template import User, Booking, BookingList

def printBooking(user=User(), bookingLog=importBooking()):
    print("here is all your bookings:")
    printList = []
    for i in bookingLog:
        printList.extend(bookingLog[i].myIncomingBooking())
    for i in printList:
        i.printBooking()