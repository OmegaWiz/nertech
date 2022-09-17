'''
DESCRIPTION
use findBooking() to retrieve the booking to be removed and remove such booking

RETURN VALUE
"successful" if remove is successful
error message if error
''' 

from importBooking import importBooking
from importUser import importUser
from template import User, Booking, BookingList


def removeBooking(user=User(), bookingLog=importBooking()):
    from findBooking import findBooking
    (room, bookingId) = findBooking(user, bookingLog)
    for i in range(0, len(bookingLog[room].getList())):
        print(bookingLog[room].getList()[i].getBookingId())
        if bookingLog[room].getList()[i].getBookingId() == bookingId:
            bookingLog[room].getList().pop(i)
            break
    print("remove",  bookingId, "successful")
    return bookingLog