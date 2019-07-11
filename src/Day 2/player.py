# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    """
    This is the travel method
    """

    def travel(self, direction):
        # Check if there's a valid room in the direction
        # getattr syntax means self.current_room.{some letter}_to
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

    """
    This is the show inventory method
    """

    def show_inventory(self):
        print(
            f'Your Inventory: {", ".join([item.name for item in self.items])}')

    """
    This is the on_take method:
    The name of an item (string) is passed as the room_item argument. 
    If this string matches the name of an item in the current room's items list,
    the item will be added to the player's items list and removed from the room.
    """

    def on_take(self, room_item):  # room_item will be a string
        for item in self.current_room.items:
            if item.name.lower() == room_item.lower():
                self.items.append(item)
                self.current_room.items.remove(item)

                item_message = f"""
                \nYou have picked up "{item.name}"
                \nYour Items: {", ".join([item.name for item in self.items])}
                \nRoom Items: {", ".join([item.name for item in self.current_room.items])}
                \n----------------------------------\n"""

                print(item_message)

            else:
                print("This item is not available in this room.")

    """
    This is the on_drop method:
    The name of an item (string) is passed as the player_item argument. 
    If this string matches the name of an item in the players's items list,
    the item will be added to the current room's items list and removed from the player.
    """

    def on_drop(self, player_item):  # player_item will be a string
        for item in self.items:
            if item.name.lower() == player_item.lower():
                self.items.remove(item)
                self.current_room.items.append(item)

                item_message = f"""
                \nYou have dropped "{item.name}"
                \nYour Items: {", ".join([item.name for item in self.items])}
                \nRoom Items: {", ".join([item.name for item in self.current_room.items])}
                \n----------------------------------\n"""

                print(item_message)

            else:
                print("You do not have this item.")
