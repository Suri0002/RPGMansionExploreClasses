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
import random


class Item:
    def __init__(self, description):
        self.description = description
    def print_description(self):
        print(self.description)

class Cat(Item):
    def __init__(self, description, location):
        Item.__init__(self, description)
        self.loc = location
    def keep_cat(self):
        print("You caught the cat.")

# Function


def choose_loc():
    ''' The function randomly choose a y-position
    and a x-position to create the cats' location.
    '''
    yloc = random.choice([0, 1, 2])
    xloc = random.choice([0, 1, 2])
    location = [yloc, xloc]
    return location


# Create pets object
cat1 = Cat("You've found a black cat", choose_loc())
cat2 = Cat("You've found a black cat", choose_loc())
cat3 = Cat("You've found a black cat", choose_loc())
pets = [cat1, cat2, cat3]

# Create a hint object
hint = Item("Two people walk in the night, whispering a story." +
            " The Queen is free and leaves behind her roses." + 
            " The King is trapped in his throne. And the Knight" +
            " keeps crossing the forest but finds nothing.\n"
           )