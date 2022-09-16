'''
DESCRIPTION
use findBooking() to retrieve the booking to be removed and remove such booking

RETURN VALUE
"successful" if remove is successful
error message if error
''' 

import loginCheck
import csv
from template import Booking, User, BookingList
def removeBooking(self, user):
    with open('bookingTable') as table:
        reader_table = csv.reader(table)
        for row in reader_table:
            if loginCheck.uid in row:
                print(row)