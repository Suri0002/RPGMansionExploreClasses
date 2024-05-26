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


class Inventory():
    def __init__(self):
        self.inventory = []
    def view_inventory(self):
        ''' The function will trigger when player choose 'inventory'.
        It will print out items in inventory if player has any in there.
        '''
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print(f"*{item}")
        else:
            print("You have nothing in your inventory.")
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

class Item():
    def __init__(self, description, location):
        self.description = description
        self.loc = location    
    def print_description(self):
        print(self.description)

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
cat1 = Item("You've found a black cat", choose_loc())
cat2 = Item("You've found a black cat", choose_loc())
cat3 = Item("You've found a black cat", choose_loc())
pets = [cat1, cat2, cat3]

# Create a hint object
hint = Item("Two people walk in the night, whispering a story." +
            " The Queen is free and leaves behind her roses." + 
            " The King is trapped in his throne. And the Knight" +
            " keeps crossing the forest but finds nothing.\n", None
           )

# Create an inventory object
inventory = Inventory()