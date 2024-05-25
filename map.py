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
from tabulate import tabulate


class Map:
    def __init__(self, map):
        self.map = map
        self.mapfile = 'map.txt'
    
    def WriteMap(self):
        ''' The function will write map to an external file'''
        try:
            with open(self.mapfile, "w") as file:
                file.write(tabulate(self.map, tablefmt = "simple_grid"))
        except:
            print("Oops! Can't write to file")
        else:
            print("Mansion map has been created.")
        finally:
            print("Good luck!")
    def ReadMap(self):
        ''' The function will read a file and print out the map'''
        try:
            with open(self.mapfile, "r") as file:
                print(file.read())
        except:
            print("Map can't be read!")
        else:
            print("Here is the map of this mansion!")
        finally:
            print("Let's explore!!" + "\n")
    def ShowMap(self):
        ''' The function calls other functions to write and
        read the map
        '''
        self.WriteMap()
        self.ReadMap()

# Create class for rooms
class Room:
    def __init__(self, description, option):
        self.description = description
        self.option = option

# Create each rooms as an object
livingroom = Room("You're in the living room", 
                  ["south"])
mainHall = Room("You're standing in the main hall",
                ["north", "south", "east"])
gallery = Room("You're in a gallery",
               ["north"])
office = Room("You're in an old-style office",
              ["south"])
hallway = Room("You're walking down a hallway, with paintings " +
               "hanging on both walls.",
               ["north", "south", "east", "west"])
dining = Room("You're in a dining room", 
              ["north", "east"])
bedroom = Room("You're in a bedroom", 
               ["south"])
hallway1 = Room("You're walking in a hallway",
                ["north", "south", "west"])
kitchen = Room("You're in a kitchen", 
               ["north", "west"])

# Mansion rooms array
room = [
    [livingroom, office, bedroom],
    [mainHall, hallway, hallway1],
    [gallery, dining, kitchen]
]

# Mansion map array
map = [
    ["living room", "office", "bedroom"],
    ["main hall", "hallway", "hallway1"],
    ["gallery", "dining room", "kitchen"]
]

# Create a map object
map1 = Map(map)