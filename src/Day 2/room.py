# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        str = f"""
              \nYour location:
              \n{self.title}
              \n   Description: {self.description}
              \n   Availabile Items: {", ".join([item.name for item in self.items])}
              \n----------------------------------\n"""
        return str
