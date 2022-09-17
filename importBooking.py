from base64 import encode
from fileinput import close, filename
from template import User, Booking, BookingList


def importBooking(fileName="./bookingLog.csv"):
    import csv
    import template
    import datetime

    bookingLog = {}
    with open(fileName, 'r') as file:
        stdread = csv.reader(file)
        for row in stdread:
            if row[1] in bookingLog.keys():
                bookingLog[row[1]].addBooking(booking=Booking(user=row[0], room=row[1], beginTime=datetime.datetime.fromisoformat(row[2]), endTime=datetime.datetime.fromisoformat(row[3]), bookingId=row[4]))
            else:
                bookingLog[row[1]] = BookingList(name=row[1], list=[Booking(user=row[0], room=row[1], beginTime=datetime.datetime.fromisoformat(row[2]), endTime=datetime.datetime.fromisoformat(row[3]), bookingId=row[4])])
            print('booking imported: ' + row[4])
    close()
    print("successfully import all bookings")
    return bookingLog

importBooking()