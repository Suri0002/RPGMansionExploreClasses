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
import sys


# Create parent class
class Item:
    def __init__(self, description):
        self.description = description
    def print_description(self):
        ''' The function print out item's description. '''
        print(self.description)
    def answer(self):
        ''' The function takes user input for answer. Player win
        if they answer correctly and the program will stop. If 
        player type quit, the program will stop.
        '''
        answer_input = input("Enter 4 numbers: ").lower()
        if answer_input == "quit":
            sys.exit("Thank you for playing!")
        if answer_input == "0903":
            print("Congrats you opened the box.")
            sys.exit("Thank you for playing!")
        else:
            print("You can't open the box. Try again!")

# Create a child class from Item
class Cat(Item):
    def __init__(self, description, location):
        Item.__init__(self, description)
        self.loc = location       

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