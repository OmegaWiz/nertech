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

from template import Booking, User, BookingList

def addBooking( user=User(), bookingLog=[Booking()]):
    import csv
    from fileinput import filename
    
    import datetime

    fileName = "roomList.csv"
    roomList = {}
    with open(fileName, 'r') as file:
        stdread = csv.reader(file)
        for row in stdread:
            roomList[row[0]] = (row[1], row[2])
    room = input('enter the room you would like to book:')
    while not room in roomList:
        print('this is not a room, please try again')
        room = input('enter the room you would like to book:')

    print('which date would you like to book?')
    print(user.getRank())
    maxDate = user.getRank() + 2
    for i in range(0, maxDate + 1):
        print(i, ": ", datetime.date.today() + datetime.timedelta(days=i))
    dayFromNow = int(input())
    while not dayFromNow in range (0, maxDate + 1):
        print("the selected date is unavailable, please try again")
        dayFromNow = int(input())
    openTime = [(datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day + dayFromNow), datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day + dayFromNow), 23, 59)]
    #remove close time
    #remove booked time
    #enter time for booking