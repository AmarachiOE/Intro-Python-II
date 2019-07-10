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

new_player = Player(player_name, room["outside"]) # Player(name, current_room)
print(f'Welcome {player_name}! Read the room descriptions to navigate to the treasure! \nYour current location is: {new_player.current_room}')


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
    player_move = input("Type n/e/s/w to move or q to quit the game: ")
    
    if player_move in move_choices:
        """
        Setting new room for when player makes a move
        """
        if player_move == "n":
            # when player moves north
            #new_room = room[new_player.current_room].n_to
            new_room = new_player.current_room.n_to

        elif player_move == "e":
            # when player moves east
            new_room = new_player.current_room.e_to
        
        elif player_move == "s":
            # when player moves south
            new_room = new_player.current_room.s_to
        
        elif player_move == "w":
            # when player moves west
            new_room = new_player.current_room.w_to

        """
        Now change new_player's current_room to the new_room_name
        """
        
        new_room_name = ""
        for key, value in room.items(): # for each key:value item in room dictionary:
            if value == new_room: # new_room is the variable/info being set from above statements
                new_room_name = key # set the name of the new room to the key of that value
        # print("Name of New Room: ", new_room_name) # double check that this is correct
        new_player = Player(player_name, room[new_room_name]) # Cool. Pass in the name of the new room to update the player's room in Player class

    elif player_move == "q":
        print(f'Thanks for playing, {player_name}!')
        break
    
    else:
        print("Invalid key. Please type n/e/s/w to move or q to quit the game.")
    
    #print(f'Your new location is: {new_room}') # or:
    print(f'Your new location is: {new_player.current_room}') # also double checks that update was successful
    


    # EXTRA NOTES
    # tried using line comprehension to set new room location for player but format was ['room name'] instead of regular 'room name' so went with a different approach
    # room_name = [key for key, value in room.items() if value == new_room] # in weird format...
    # new_player = Player("Amarachi", room_name)
    # print("Room_Name: ", room_name)