# define an item class
# items will be objects in the rooms
# as well as objects in player inventory

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'