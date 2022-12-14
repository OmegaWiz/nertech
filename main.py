import datetime
from importUser import importUser
from importBooking import importBooking
from removeBooking import removeBooking
from template import Booking, User, BookingList
from createUser import createUser
from loginCheck import loginCheck
from removeBooking import removeBooking
from saveUser import saveUser
from saveBooking import saveBooking

userLog = importUser()
bookingLog = importBooking()
(user, userLog) = loginCheck(userLog)

while(True):
    mode = int(input('What would you like to do today?\n0 - quit program\n1 - add a new booking\n2 - remove a booking\n3 - check your booking\n4 - change user\n'))
    if(mode == 0):
        saveUser(userLog=userLog)
        saveBooking(bookingLog=bookingLog)
        print("thank you!")
        break
    elif(mode == 1):
        #addBooking()
        print()
    elif(mode == 2):
        bookingLog = removeBooking(user, bookingLog)
    elif(mode == 3):
        #printBooking(user)
        print()
    elif(mode == 4):
        uid = loginCheck(userLog)