import datetime

from template import Booking, User
#from addBooking import *
#from checkBooking import *
#from printBooking import *
#from removeBooking import *
from createUser import createUser
from loginCheck import loginCheck

testUser = User("test", "test", 1)
teacherUser = User('teacher', 'teacher', 5)
adminUser = User('admin', 'admin', 10)

userLog = {
    "test": testUser,
    "teacher": teacherUser,
    "admin": adminUser
}

userLog = loginCheck(userLog)

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
        #checkBooking(uid)
        print()
    elif(mode == 4):
        uid = loginCheck(userLog)