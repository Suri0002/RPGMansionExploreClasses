

class Item:
    def __init__(self, description, location):
        self.description = description
        self.loc = location

class Cat(Item):
    def __init__(self, description, location):
        Item.__init__(self, description, location)
    def keep_cat(self):
        print("You caught the cat.")

class Hint(Item):
    def __init__(self, description, location):
        Item.__init__(self, description, location)


                
cat1 = Cat("You've found a black cat", [0,0])
cat2 = Cat("You've found a black cat", [2,1])
items = [cat1, cat2]

hint = Hint("Two people walk in the night, whispering a story." +
            " The Queen is free and leaves behind her roses. The King" + 
            " is trapped in his throne. And the Knight keeps crossing" +
            " the forest but finds nothing.", None)
