'''
DESCRIPTION
attempts to add booking with time period as it has input
if the time slot requested is available, add the requested booking into bookingLog
    and tells the user that booking is successful
if it is unavailable but is overridable, ask if user wants to override, 
    if so, calls overrideBooking(user, oldBooking, newBooking, bookingLog)
on other cases denies the booking, print error message, and return failed

RETURN VALUE
upon successful booking, it should return "successful"
if overrideBooking is called, return the value from 
    overrideBooking(user, oldBooking, newBooking, bookingLog)
otherwise, return "failed"
''' 

from template import Booking, User
import datetime

def addBooking( user=User(),
                bookingLog=[Booking()]):

    possibleRoom = ['c1', 'c2', 'l1', 'l2', 'l3', 'l4', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7',
    'm8', 'm9', 'w1', 'w2', 'w3', 'w4', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8']
    room = input('enter the room you would like to book:')
    while not room in possibleRoom:
        print('this is not a room, please try again')
        room = input('enter the room you would like to book:')
    print('which date would you like to book?')
    maxDate = user.printRank() + 2
    for i in range(0, maxDate + 1):
        print("{i}: {datetime.date.today() + datetime.timedelta(days=i)}")
    dayFromNow = int(input())
    while not dayFromNow in range (0, maxDate + 1):
        print("the selected date is unavailable, please try again")
        dayFromNow = int(input())

    #enter time for booking