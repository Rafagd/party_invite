import coords

# Class representing a Customer
# I'm using it as a data object 
class Customer:
    user_id = None
    name    = None
    coords  = None

    # Constructor
    def __init__(self, user_id, name, coords):
        self.user_id = user_id
        self.name    = name
        self.coords  = coords

    def __str__(self):
        return "{{ {}: {} {} }}".format(self.user_id, self.name, self.coords)

    def __repr__(self):
        return self.__str__()
