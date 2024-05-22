######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: OOP: RPG - Classes
# Coder: Suri Ho
# Version: 4.0
######################################################################
'''
'''
######################################################################
# Import
from inventory import Item


class Message(Item):
    def __init__(self, description):
        Item.__init__(self, description)

# Create message objects
message1 = Message("You visit your grandma and receive a mystery box" +
                   " from her, but there's a four-number lock on it."
                  )
message2 = Message("Her cats have kept the hint papers, so help her"+
                   " find the cats and get the hint to open the box."
                  )
message3 = Message("You can type 'quit' to exit the game at any "+
                   "point.\n"
                  )

# Function


def instruction():
    ''' The function print messages to the console.'''
    message1.print_description()
    message2.print_description()
    message3.print_description()