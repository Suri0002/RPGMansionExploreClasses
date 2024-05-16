import sys


class Player:
    def __init__(self):
        self.y = 1
        self.x = 0
        self.inventory = []
        self.action = ["go", "quit", "map", "look", "inventory"]
    def move_input(self):
        self.way = input("Which direction do you want to go? ").lower()
        if self.way == "quit":
            sys.exit("Thanks for playing.")
        else:
            self.move(self)
    def move(self, way):
        if way == "n":
            self.y -= 1
        elif way == 's':
            self.y += 1
        elif way == 'e':
            self.x += 1
        elif way == 'w':
            self.x -= 1


def main_menu():
    player = Player()
    
    