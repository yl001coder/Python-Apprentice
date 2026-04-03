"""
Functions needed:
welcome + check-in
upgrade
room service
main
asking questions for the welcome func
check-out

Returns:
welcome: room #, name, length of stay, how many rooms
upgrade: what upgrade
room service: resources needed
asking questions: question answers
check-out: room checked out of

Using:
print & input

Need: list of rooms

Imports:
Random

"""
hotel_is_open = True

rooms = [101,102,103,104,105,106,107,108,109]
rooms_taken = list()
guest_book = dict()
days = int()
menu = ["jellybears", "strawberry cones", "crystal jellies","omurice"
        "cake roll"]
name_night = dict()
guest = list()

def main():
    #main function
    while(hotel_is_open == True):

        hotel_stuff()

def hotel_stuff():
    """
    does hotel stuff 
    
    """
    welcomes()

    room_service("Wind Archer Cookie")
    time_pass()

def welcomes():
    """
    returns: gets name, #of nights, #of rooms

    Functionality:
    asks guest for their name (to store it in a guestbook/dictionary)
    and asks them for the number of rooms that they want to check into

    returns: 
    number of nights the guest is staying

    functionality:
    asks guests for the number of nights they are staying,
    and attributes that to the guest's name in the guestbook (dictionary)

    """

    if(len(rooms)==0):
        return None
    #welcomes guests, and helps them check-in
    print("Hi, I'm Gingerbrave, and welcome to the Earthbread Hotel!")
    name = input("What is your name? ")
    
    no_of_rooms = True

    nights = input("And, how many nights will you be staying? ")
    guest_book[name] = nights
    name_night[name] = days
 
 
    while(no_of_rooms == True):
        roooms = input("Additionally, how many rooms would you like to book? ")
        if(int(roooms)>len(rooms)):
            print("Unfortunately, we don't have that many open rooms at the moment.")
        else:
            no_of_rooms = False


    print("Alright. Your room numbers will be: ")
    for i in range(int(roooms)):
        print(rooms[0])
        rooms_taken.append(rooms[0])
        rooms.remove(rooms[0])

    return nights, name

def want_fud(guest):
    """
    ask guest if want food

    returns: Y/N
    
    """

    foodYN = input(guest+ ", would you like some food now that you've checked in? (yes/no input) ")
    if(foodYN.lower == "yes"):
        return True
    elif():
        return False

def room_service(name):
    """
    room service function for fun later

    returns:
    what the guest wants to eat
    
    """
    fuds = input("Food! (press enter)")
    print("Here's the menu:")
    for i in range(4):
        print(menu[i])

    food = input(name + ", what would you like to eat? ")
    l = menu.split()
    for i in l:
        if(food in menu):
            print("Here is your " + food)
            return food
    return False

def time_pass():
    """ 
    function: to keep track of days to check guests out and in
    runs functions for each day 

    iwfilwyoaoaidchwownmhlibym
    
    i

    """
    days = 1
    welcomes()
    room_service(guest[0])

def check_out(guest):
    """
    function:
    checks-out guests by seeing when
    int(name_night[name]) - int(guest_book[name]) = 0
    to check them out

    guests == the guest list
    
    """
    for i in len(guest):
        if((name_night[guest[i]]) - int(guest_book[guest[i]]) == 0):
            print("Thank you for staying " + guest + "!")
            del guest_book[str(guest)]
        
"""


"""

main()