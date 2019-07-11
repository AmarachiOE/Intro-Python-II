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
    This is the get method
    """    
    def get_item(self, room_item):
        for item in self.current_room.items:
            if item.name.lower() == room_item.lower():
                self.items.append(item)
                print(f'Your Items: {", ".join([item.name for item in self.items])}')
            
            else:
                print("This item is not available in this room.")