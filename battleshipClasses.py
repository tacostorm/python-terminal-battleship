class Player:
    
    idCounter = 0

    def __init__(self):
        self.id = Player.idCounter
        self.play_area = PlayArea()
        self.ships = []
        Player.idCounter += 1

    def __repr__(self) -> str:
        print("Player {id}".format(id=self.id + 1))
    
    def reset(self):
        pass

    def attacks(self, target, coordinate):
        pass

class PlayArea:
    
    def __init__(self, height = 10, length = 10):
        self.height = height
        self.length = length
        self.modules = []
        for row in range(self.height):
            row_info = []
            for column in range(self.length):
                temp = chr(row+65) + str(column+1)
                row_info.append(Module(temp))
                #print(temp)
            self.modules.append(row_info)
    
    def show(self, owner_perspective = True):
        display_string = ""
        for row in range(self.height):
            for column in range(self.length):
                
                display_string += "~ " #self.modules[row][column].coordinates + "\t"
            display_string += "\n"
        return display_string

class Module:

    def __init__(self, coordinates="", contents="", isGuessed = False):
        self.contents = contents
        self.isGuessed = isGuessed
        self.coordinates = coordinates

    def __repr__(self):
        return "{coordinates} contains {contents}. isGuessed = {isGuessed}".format(coordinates = self.coordinates, contents = self.contents, isGuessed = self.isGuessed)
    
class Ship:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.health = size
        self.isDestroyed = False
        self.position = ""
        self.orientation = ""

    def __repr__(self):
        return "{name} of size {size}".format(name = self.name, size = self.size)