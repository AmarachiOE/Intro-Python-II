# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """
    This is a Room class that stores name, description, and n/s/e/w orientation
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    """
    This method will print out a string of the Room class object
    """ 
    def __str__(self):
        return f'"{self.name}" \n Description: "{self.description}"'