# 1 internal file
# 2 external file
# 3a Database 
# 3b online
#   upload file 
# 3c interface

''' data type
id string "08155"
room
    library C1, C2, L1 - L4
    washing machine (9, 4) M1 - M9, W1 - W4 
    music (8) M1 - M8
date
    YYYYMMDD
time
    (H, M)
Duration
    integer (minutes)
'''

def checkBooking(id, room, date, time, duration):
    '''
    check if book-able
    teacher - 7 days early
    student - 3 days early
    '''
    print("yes")

def addBooking(id, room, date, time, duration):
    #book a reservation for this id
    print("yes")

def printBooking(id):
    #display all booking of this id
    print("yes")

def removeBooking(id, room, date, time, duration):
    #cancel a booking
    print("yes")

def main():
    #main interface for program
    print("Please enter your ID:")
