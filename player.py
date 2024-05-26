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

import map


class Player:
    def __init__(self):
        self.y = 1
        self.x = 0
        self.action = ["go", "quit", "map", "look", "inventory", "answer"]
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
        ''' The function takes player input for a direction and update
        player's y and x location. If player choose quit, the program 
        will stop.
        '''
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
            else:
                print("You can't go that way.") 
    def location(self):
        ''' The function returns player's y and x location as list. '''
        return [self.y, self.x]


# Create a player object
player = Player()