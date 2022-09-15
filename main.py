def checkBooking(uid, room, date, time, duration):
    '''
    check if book-able
    teacher - 7 days early
    student - 3 days early
    '''
    print("yes")

def addBooking(uid, room, date, time, duration):
    #book a reservation for this id
    print("yes")

def printBooking(uid):
    #display all booking of this id
    print("yes")

def removeBooking(uid, room, date, time, duration):
    #cancel a booking
    print("yes")

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