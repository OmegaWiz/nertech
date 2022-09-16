'''
DESCRIPTION
print all, incoming, or next booking of the user

RETURN VALUE
none
'''

import loginCheck
import csv
from template import Booking, User, BookingList
def printBooking():
    with open('bookingTable.csv') as table:
        reader_table = csv.reader(table)
        for row in reader_table:
            if loginCheck.uid in row:
                print(row)