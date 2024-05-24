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
# Imports
import sys

import inventory as inv
import map
import message as mes


class Player:
    def __init__(self):
        self.y = 1
        self.x = 0
        self.inventory = []
        self.action = ["go", "quit", "map", "look", "inventory"]
        self.loc = map.room[self.y][self.x]

    def current_loc(self):
        ''' The function updates player's location and print
        the current room's description
        '''
        self.loc = map.room[self.y][self.x]
        print(self.loc.description)
    def print_action(self):
        ''' The function prints action option to the console'''
        for action in self.action:
            print(f"-{action}")            
    def move(self):
        ''' The function takes player'''
        while True:
            print("Direction option(s): ")
            for option in self.loc.option:
                print(f"* {option}")
            # Get player's input for a direction
            way = input("Which direction do you want to go? ").lower()
            if way == "quit":
                sys.exit("Thanks for playing.")
            else:
                if way in self.loc.option:
                    if way == "north":
                        self.y -= 1
                    elif way == "south":
                        self.y += 1
                    elif way == "east":
                        self.x += 1
                    elif way == "west":
                        self.x -= 1
                    break
                else:
                    print("You can't go that way." + "\n")
                
    def view_inventory(self):
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print(f"*{item}")
        else:
            print("You have nothing in your inventory.")
           
    def inspect_Room(self):
        ''' The function will trigger when user choose 'look'. If there is
        an object at their location, description will be printed. If there
        is no interactive piece, a message will be printed.
        '''
        object_found = False
        room_inventory = []
        # Print item's description if it's at player's current location
        try:
            for object in inv.pets:
                object_y = object.loc[0]
                object_x = object.loc[1]
                if object_y == self.y and object_x == self.x:
                    print(object.description)
                    object_found = True
                    room_inventory.append(object)
        except:
            print("You find nothing here.")
        else:
            if object_found is True:
                for item in room_inventory:
                    if item == inv.cat1 or item == inv.cat3:
                        self.inventory.append("cat")
                        item.keep_cat()
                        inv.pets.remove(item)
                    if item == inv.cat2:
                        self.inventory.append("cat")
                        inv.cat2.keep_cat()
                        inv.pets.remove(inv.cat2)
                        self.get_hint()
            else:
                print("There is nothing suspicious in the room.\n")
    def get_hint(self):
        self.inventory.append("hint")
        mes.message4.print_description()
        self.action.append("answer")
    def hint(self):
        inv.hint.print_description()
    def answer(self):
        answer_input = input("Enter 4 numbers: ").lower()
        if answer_input == "quit":
            sys.exit("Thank you for playing!")
        if answer_input == "0903":
            print("Congrats you opened the box.")
            sys.exit("Thank you for playing!")
        else:
            print("You can't open the box. Try again!")