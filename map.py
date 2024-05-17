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

class Room:
    def __init__(self, description, option):
        self.description = description
        self.option = option

# Create each rooms as an object
livingroom = Room('''You're in the living room''', ["s"])
mainHall = Room('''You're standing in the main hall''', ["n", "s", "e"])
gallery = Room('''You're in a gallery''', ["n"])
office = Room('''You're in an old-style office''', ["s"])
hallway = Room('''You're walking down a hallway, with paintings
                hanging on both walls.''', ["n", "s", "e", "w"])
dining = Room('''You're in a dining room''', ["n", "e"])
bedroom = Room('''You're in a bedroom''', ["s"])
hallway1 = Room('''You're walking in a hallway''', ["n", "s", "w"])
kitchen = Room('''You're in a kitchen''', ["n", "w"])

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

# Functions
def showMap():
    map1 = Map(map)
    map1.WriteMap()
    map1.ReadMap()