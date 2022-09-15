import datetime

from addBooking import *
from checkBooking import *
from printBooking import *
from removeBooking import *

def main():
    uid = input('please enter your id: ')
    print('Welcome, ' + uid + '!')
    mode = int(input('What would you like to do today?\n0 - quit program\n1 - add a new booking\n2 - remove a booking\n3 - check your booking\n'))
    if(mode == 0):
        print("thank you!")
        return
    elif(mode == 1):
        addBooking()
    elif(mode == 2):
        removeBooking()
    elif(mode == 3):
        checkBooking(uid)

main()