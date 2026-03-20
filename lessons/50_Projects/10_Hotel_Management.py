"""
Functions needed:
welcome + check-in
upgrade
room service
main
asking questions for the welcome func
buttons(?)
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
"""
hotel_is_open = True

rooms = [101,102,103,104,105,106,107,108,109]
rooms_taken = list()

def main():
    #main function 
    print("")
    welcome()

def welcome():
    if(len(rooms)==0):
        return None
    #welcomes guests, and helps them check-in
    print("Welcome to the Earthbread Hotel!")
    name = input("What is your name? ")
    m = True
    while(m == True):
        room_numbers = input(name + ", how many rooms would you like to check into? ")
        if(int(room_numbers)>len(rooms)):
            print("Unfortunately, we don't have that many open rooms at the moment.")
        else:
            m = False
    print("Your room numbers will be: ")
    for i in range(int(room_numbers)):
        rooms.remove("10"+str(i))
        print(rooms[i])
    nights = input("And, how many nights will you be staying? ")
    print("Okay! Check out is at 9:00 AM")

    #successful func

main()