from room import Room
from player import Player
from item import Item

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
player = Player(player_name, room['outside']) # Player(name, current_room)
current_room = player.current_room


# Create Items
binoculars = Item("Binoculars", "Use the binoculars to see far away places")
flashlight = Item("Flashlight", "Use the flashlight to see in dark places.")
boots = Item("Boots", "You may want these boots for your journey.")
water = Item("Water", "Drink water if you're tired!")
#print(binoculars.name, flashlight.name, water.name)

# Add Items to Room and Player
room["outside"].items.append(binoculars)
room["outside"].items.append(boots)
room["foyer"].items.append(flashlight)
player.items.append(water)

print(f'Welcome, {player_name}! Read the room descriptions to navigate to the treasure! \n{current_room}')

move_choices = ["n", "s", "e", "w"]



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

while True:
    # Wait for user input

    # Record how many words the user entered (1 or 2?)
    # NOTE: .lower()[0] converts input to lowercase and only takes the first character to ultimately match move_choices list items
    cmd = input(">>> ")
    input_count = len(cmd.split())
    print("Input Count: ", input_count)

    # If input_count = 1 treat as navigation command:
    if input_count == 1:
        cmd = cmd.lower()[0] # convert to lowercase and only take 1st letter
        # Parse user inputs (n, s, e, w, q)
        if cmd in move_choices:
            # If input is valid, move the player and loop
            player.travel(cmd)
        elif cmd == "q":
            print(f'Thanks for playing, {player_name}!\n')
            exit() # or break
        else:
            print("Invalid key. Please type North, East, South, or West to move or q to quit the game.")

    # If input_count = 2 treat as action command:
    elif input_count == 2:
        # handle actions
        print("Some action")
    
    else:
        pass
    