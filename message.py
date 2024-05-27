######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: OOP: RPG - Classes
# Coder: Suri Ho
# Version: 4.0
######################################################################
''' Instructions and story line for the game so user knows the tasks
and goal of the game.
'''
######################################################################
# Import
from inventory import Item


# Create a child class from Item
class Message(Item):
    def __init__(self, description, location):
        Item.__init__(self, description, location)


# Create message objects
message1 = Message("You visit your grandma and receive a mystery box "
                   + "from her, with a four-digit lock on it.", None)
message2 = Message("One of her three cats has kept the hint paper, so "
                   + "help her find the cat and get the hint to open "
                   + "the box.", None)
message3 = Message("Type 'open' to enter the numbers.", None)
message4 = Message("You can type 'quit' to exit the game at any "
                   + "point.\n", None)

# Create a list of messages 
instruction = [message1, message2, message3, message4]