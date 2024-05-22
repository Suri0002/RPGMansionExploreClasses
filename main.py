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

from map import showMap
from message import instruction
from player import Player

# Function


def main_menu():
    instruction()
    player = Player()
    while True:
        player.current_loc()
        player.print_action()
        action_input = input("What do you want to do? ").lower()
        if action_input == "quit":
            sys.exit("Thank you for playing!")
        if action_input == "go":
            player.move()
        if action_input == "map":
            showMap()
        if action_input == "look":
            player.inspect_Room()
        if action_input == "inventory":
            player.view_inventory()
        if action_input == "answer":
            player.answer()


main_menu()