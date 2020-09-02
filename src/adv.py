from room import Room
from player import Player

# Declare all the rooms
# dictionary of room objects

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']

# test = Player('Nate', outside)
# print(test.current_room.n_to.name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please enter your player name: ')
print('------------------------------------')
print('------------------------------------')


player = Player(name, outside)

x = 0
# Write a loop that:
while x == 0:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(player)
    print('------------------------------------')
    print('------------------------------------')
    # * Waits for user input and decides what to do.
    print('What direction would you like to go?')
    direction = input('Your options are n, s, e, w, or q to quit: ')
    print('------------------------------------')
    print('------------------------------------')
    
    x += 1

    while x == 1:
    # If the user enters a cardinal direction, attempt to move to the room there.
        print(f'You chose {direction} as your direction')
        print(player.current_room)
        print('------------------------------------')

        if direction == 'n':
            north_room = player.current_room.n_to
            if north_room != 'unknown':
                player.current_room = north_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')


        elif direction == 's':
            south_room = player.current_room.s_to
            if south_room != 'unknown':
                player.current_room = south_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        elif direction == 'e':
            east_room = player.current_room.e_to
            if east_room != 'unknown':
                player.current_room = east_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        elif direction == 'w':
            west_room = player.current_room.w_to
            if west_room != 'unknown':
                player.current_room = west_room
                print('------------------------------------')
                print('------------------------------------')
                x = 0

            else:
                direction = input("You can't go that way. Try another direction: ")
                print('------------------------------------')
                print('------------------------------------')

        # If the user enters "q", quit the game.
        elif direction == 'q':
            print('Thanks for playing!')
            x = 2
        
        else:
            print('Unfortunately, that is an invalid direction!')
            direction = input('Your options are n, s, e, w, or q to quit: ')
            print('------------------------------------')
            print('------------------------------------')            




#

# Print an error message if the movement isn't allowed.
#

