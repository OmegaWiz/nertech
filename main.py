import datetime
from importUser import importUser
from template import Booking, User, BookingList
from createUser import createUser
from loginCheck import loginCheck

userLog = importUser()

bookingLog = {'00': BookingList()}

(user, userLog) = loginCheck(userLog)

while(True):
    mode = int(input('What would you like to do today?\n0 - quit program\n1 - add a new booking\n2 - remove a booking\n3 - check your booking\n4 - change user\n'))
    if(mode == 0):
        print("thank you!")
        break
    elif(mode == 1):
        #addBooking()
        print()
    elif(mode == 2):
        #removeBooking()
        print()
    elif(mode == 3):
        #printBooking(user)
        print()
    elif(mode == 4):
        uid = loginCheck(userLog)