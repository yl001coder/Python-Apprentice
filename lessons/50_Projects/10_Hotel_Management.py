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

def main():
    #main function
    while(hotel_is_open == True):

        welcome()

def welcome():
    name()
    num_of_nights()
    room_numbers()
    room_service()

def name():
    """
    returns: name

    Functionality:
    asks guest for their name (to store it in a guestbook/dictionary)
    and asks them for the number of rooms that they want to check into

    """

    if(len(rooms)==0):
        return None
    #welcomes guests, and helps them check-in
    print("Hi, I'm Gingerbrave, and welcome to the Earthbread Hotel!")
    name = input("What is your name? ")
    if(name == "dark enchantress cookie"):
        print("!!ANNOUNCEMENT!! /n" \
        "we are currently shutting down the Earthbread Hotel /n" \
        "due to safety reasons. /n" \
        "Thank you!")

        hotel_is_open == False

    
    no_of_rooms = True
    while(no_of_rooms == True):
        room_numbers = input(name + ", how many rooms would you like to check into? ")
        if(int(room_numbers)>len(rooms)):
            print("Unfortunately, we don't have that many open rooms at the moment.")
        else:
            no_of_rooms = False
    
    return name
    
def num_of_nights():
    """
    returns: 
    number of nights the guest is staying

    functionality:
    asks guests for the number of nights they are staying,
    and attributes that to the guest's name in the guestbook (dictionary)

    """

    nights = input("And, how many nights will you be staying? ")
    guest_book[name] = nights
    return nights

def room_numbers():
    """"
    returns:
    none (because the rooms/rooms taken will be stored in a list)

    functionality"
    gives the guest a certain amount of room numbers based off
    of how many rooms they chose to check into earlier

    """

    print("Your room numbers will be: ")
    for i in range(int(room_numbers)):
        print(rooms[0])
        rooms_taken.append(rooms[0])
        rooms.remove(rooms[0])

def room_service(name):
    """
    room service function for fun that will be implemented later

    returns:
    what the guest wants to eat from room service
    
    """
    print("Here's the menu:")
    for i in range(5):
        print(menu[i])

    food = input(name + "What would you like to eat?")
    l = menu.split()
    for i in l:
        if(i in menu):
            return food
    return False

    



main()