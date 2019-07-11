from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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
# setting the n_to/s_to/etc. attr on various Room class instances to another instance of Room
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = room['overlook']
room['overlook'].e_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Please type your name: ")

player = Player(player_name, room["outside"]) # Player(name, current_room)
print(f'Welcome {player_name}! Read the room descriptions to navigate to the treasure! \nYour current location is: {player.current_room}')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
move_choices = ["n", "e", "s", "w"]

while True:
    player_move = input(">>> Type North, East, South, or West to move or q to quit the game: ").lower()[0] # converts input to lowercase and only takes the first character to ultimately match move_choices list items
    print("Player Move: ", player_move)
    
    if player_move in move_choices:
        """
        Setting new room for when player makes a move
        """
        if player_move == "n":
            # when player moves north
            new_room = player.current_room.n_to
            # better way: player.current_room = player.current_room.n_to

        elif player_move == "e":
            # when player moves east
            new_room = player.current_room.e_to
        
        elif player_move == "s":
            # when player moves south
            new_room = player.current_room.s_to
        
        elif player_move == "w":
            # when player moves west
            new_room = player.current_room.w_to

        """
        Now change player's current_room to the new room
        """
        player = Player(player_name, new_room)

        """
        Alternative, Longer Way - SMH
        new_room_name = ""
        for key, value in room.items(): # for each key:value item in room dictionary:
            if value == new_room: # new_room is the variable/info being set from above statements
                new_room_name = key # set the name of the new room to the key of that value
        # print("Name of New Room: ", new_room_name) # double check that this is correct
        player = Player(player_name, room[new_room_name]) # Cool. Pass in the name of the new room to the room dictionary to update the player's room in the new player's Player class instance
        """

        
    elif player_move == "q":
        print(f'Thanks for playing, {player_name}!\n')
        break # or exit()
    
    else:
        print("Invalid key. Please type North, East, South, or West to move or q to quit the game.")
    
    #print(f'Your new location is: {new_room}') # or:
    print(f'Your new location is: {player.current_room}') # also double checks that update was successful
    


    # EXTRA NOTES
    # tried using line comprehension to set new room location for player but format was ['room name'] instead of regular 'room name' so went with a different approach
    # room_name = [key for key, value in room.items() if value == new_room] # in weird format...
    # player = Player("Amarachi", room_name)
    # print("Room_Name: ", room_name)

"""
# SEAN'S SOLUTION
def try_direction(direction, current_room):
    attribute = direction + '_to' # ex. n + _to = n_to

    # Check if inputted direction is one we can move to
    # Is it a defined option??
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        print("You can't go that way!")
        return current_room

# Then in while loop:
player.current_room = try_direction(player_move, player.current_room)
"""