from item import Item
from player import Player
from room import Room
# Create items
book = Item('Book')
knife = Item('Knife')
flashlight = Item('Flashlight')
dog = Item('Dog')

# Create a room with items
bedroom = Room('Bedroom', 'Messy', objects = [book, dog])
print(bedroom)

# Create a player with an item
player = Player('Nate', 'Bedroom', inventory=[flashlight, knife])
print(player)

# Have the player pick up the item in the room
player.grab(book)
print(player)
print(bedroom)

# Have the room drop the item
bedroom.drop_object(book)
print(bedroom)

# Have the player drop an item in the room
player.drop(knife)
bedroom.add_object(knife)
print(player)
print(bedroom)

# Have the room add the item