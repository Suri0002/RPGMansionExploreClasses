import sys
import map

class Player:
    def __init__(self):
        self.y = 1
        self.x = 0
        self.inventory = []
        self.action = ["go", "quit", "map", "look", "inventory"]

    def curren_loc(self):
        loc = 
    def print_action(self):
        for action in self.action:
            print(f"-{action}")
    def move_input(self):
        #print("Direction option(s): ")
        #for option in map.room[]:
            #print(f"* {option}")
        way = input("Which direction do you want to go? ").lower()
        if way == "quit":
            sys.exit("Thanks for playing.")
        else:
            self.move(self)
    def move(self, way):
        if way in map.room[][]:
            if way == "n":
                self.y -= 1
            elif way == 's':
                self.y += 1
            elif way == 'e':
                self.x += 1
            elif way == 'w':
                self.x -= 1
    def view_inventory(self):
        choosing = True
        while choosing:
            if self.inventory:
                print("Inventory: ")
                for item in self.inventory:
                    print(f"*{item}")
                access_choice = input("Do you want to access any item? ").lower()
                if access_choice == "quit":
                    sys.exit("Thank you for playing!")
                #if access_choice == "yes":
                    #useInventory()
                elif access_choice == "no":
                    choosing = False
                else:
                    print("Please choose yes or no.")
            else:
                print("You have nothing in your inventory.")


def main_menu():
    while True:
        player = Player()
        player.print_action()
        action_input = input("What do you want to do? ").lower()
        if action_input == "quit":
            sys.exit("Thank you for playing!")
        if action_input == "go":
            player.move_input()
        if action_input == "map":
            map.showMap()
        #if action_input == "look":
            #inventory.inspect_Room()
        if action_input == "inventory":
            player.view_inventory()


main_menu()