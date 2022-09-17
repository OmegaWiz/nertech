from template import User, Booking, BookingList
from importBooking import importBooking

def saveBooking(bookingLog=importBooking(), fileName="./bookingLog.csv"):
    import csv
    with open(fileName, 'w', encoding='UTF8', newline='') as file:
        stdwrite = csv.writer(file)
        for room in bookingLog.keys():
            for booking in bookingLog[room].getList():
                stdwrite.writerow([booking.getUser(), booking.getRoom(), booking.getBeginTime(), booking.getEndTime(), booking.getBookingId()])
            '''
            user=row[0], room=row[1], beginTime=datetime.datetime.fromisoformat(row[2]), endTime=datetime.datetime.fromisoformat(row[3]), bookingId=row[4]
            '''
    print("successfully save all bookings")