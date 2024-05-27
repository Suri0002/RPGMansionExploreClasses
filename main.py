######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: OOP: RPG - Classes
# Coder: Suri Ho
# Version: 4.0
######################################################################
''' The program allows player to go around the mansion and look for
objects in room. Player can access map and inventory at any time.
The goal is to find four numbers to open a lock on the box. A hint will
be provided, but player need to find the cat that keeps the hint out
of the three cats. Cats are placed randomly into rooms every time the 
game starts. Player can choose to quit the game at any point.
'''
######################################################################
# Imports
import sys

import inventory as inv
import map
from message import instruction
from player import player

# Function


def main_menu():
    ''' The function is the main menu for the game. It prints
    out instruction, player's location and actions and ask player
    what they want to do. If player choose quit, the program 
    will stop.
    '''
    # Print the instructions
    for mess in instruction:
        mess.print_description()
    while True:
        # Print player's current location and action options
        player.current_loc()
        player.print_action()
        # Get player's input for an action
        action_input = input("What do you want to do? ").lower()
        if action_input == "quit":
            sys.exit("Thank you for playing!")
        elif action_input == "go":
            player.move()
        elif action_input == "map":
            map.map1.ShowMap()
        elif action_input == "look":
            inv.inventory.inspect_Room()
        elif action_input == "inventory":
            inv.inventory.view_inventory()
        elif action_input == "open":
            inv.inventory.answer()
        elif "hint" in inv.inventory.inventory and action_input == "hint":
            inv.hint.print_description()
        else:
            print("Invalid action!\n")


# Main
main_menu()