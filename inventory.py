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

from player import player


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
    def get_hint(self):
        ''' The function adds hint to player's inventory and 
        prints out a message.
        '''
        self.inventory.append("hint")
        print("You've found the right cat. Hint is now in your"+
                " inventory. Type hint to see it!")
    def cat_action(self):
        ''' '''
        choosing = True
        while choosing:
            print("*catch")
            print("*done")
            cat_choice = input("Choose an action: ").lower()
            if cat_choice == "catch":
                self.inventory.append("cat")
                print("You caught the cat.")
                self.item.loc = None
                if self.item == cat2:
                    self.get_hint()
                choosing = False
            elif cat_choice == "quit":
                sys.exit("Thank you for playing!")
            elif cat_choice == "done":
                choosing = False
            else:
                print("Invalid choice. Try again.")  
                
    def inspect_Room(self):
        ''' The function will trigger when user choose 'look'. If there is
        an object at their location, description will be printed. If there
        is no interactive piece, a message will be printed.
        '''
        object_found = False
        room_inventory = []
        # Print item's description if it's at player's current location
        try:
            for object in pets:
                if object.loc == player.location():
                    print(object.description)
                    object_found = True
                    room_inventory.append(object)
        except:
            print("You find nothing here.")
        else:
            if object_found is True:
                for self.item in room_inventory:
                    self.cat_action()
            else:
                print("There is nothing suspicious in the room.")
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

# Create a class for items
class Item():
    def __init__(self, description, location):
        self.description = description
        self.loc = location    
    def print_description(self):
        print(self.description)

# Function


def choose_loc():
    ''' The function randomly choose a y-position and a 
    x-position to create the cats' location.
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
hint = Item("Two people walk in the night, whispering a story.\n" +
            "The Queen is free and leaves behind her roses.\n" + 
            "The King is trapped in his throne.\nThe Knight" +
            " keeps crossing the forest but finds nothing.", None
           )

# Create an inventory object
inventory = Inventory()