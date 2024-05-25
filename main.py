######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: RPG - Inventory
# Coder: Suri Ho
# Version: 3.0
######################################################################
''' Player can choose quit to stop.
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
    # Print the instructions
    for mess in instruction:
        mess.print_description()
    while True:
        player.current_loc()
        player.print_action()
        action_input = input("What do you want to do? ").lower()
        if action_input == "quit":
            sys.exit("Thank you for playing!")
        elif action_input == "go":
            player.move()
        elif action_input == "map":
            map.map1.ShowMap()
        elif action_input == "look":
            player.inspect_Room()
        elif action_input == "inventory":
            player.view_inventory()
        elif "answer" in player.action and action_input == "answer":
            inv.hint.answer()
        elif "hint" in player.inventory and action_input == "hint":
            inv.hint.print_description()
        else:
            print("Invalid action!\n")


main_menu()