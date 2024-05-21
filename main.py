# Imports
import sys

import map
from player import Player


def main_menu():
    player = Player()
    #inventory = Inventory()
    while True:
        player.current_loc()
        player.print_action()
        action_input = input("What do you want to do? ").lower()
        if action_input == "quit":
            sys.exit("Thank you for playing!")
        if action_input == "go":
            player.move()
        if action_input == "map":
            map.showMap()
        if action_input == "look":
            player.inspect_Room()
        if action_input == "inventory":
            player.view_inventory()
        if action_input == "answer":
            player.answer()


main_menu()