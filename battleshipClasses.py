class Player:
    
    idCounter = 1

    def __init__(self, ships = {}, height=10, length=10):
        self.id = Player.idCounter
        self.play_area = PlayArea(height, length)
        self.ships = ships
        Player.idCounter += 1
        self.max_health = 0
        for ship in self.ships:
            self.max_health += self.ships[ship].health
        self.health = self.max_health
        

    def __repr__(self) -> str:
        print("Player {id}".format(id=self.id))

    def place_ship(self, coordinates, ship):
        content = ship[0]
        for coordinate in coordinates:
            self.play_area.modules.update({coordinate:Module(coordinate, content)})
        self.ships[ship].is_placed = True   
        pass

    def get_number_unplaced_ships(self):
        unplaced_ships = 0
        for key in self.ships:
            if not self.ships[key].is_placed: 
                unplaced_ships += 1

        return unplaced_ships

    def get_ship_from_input(self, input):
        
        for ship in self.ships:
            if ship[0] == input: 
                return ship
        pass
    
    def reset(self):
        pass

    def is_alive(self):
        return self.health > 0
    
    def get_health(self):
        return self.health

    def attacks(self, enemy, coordinate):
        result = ""
        enemy.play_area.modules[coordinate].isGuessed = True
        if enemy.play_area.modules[coordinate].contents == "":
            result = "miss."
        else:
            enemy.health -= 1
            result = "hit!"
        return result

class PlayArea:
    
    def __init__(self, height = 10, length = 10):
        self.height = height
        self.length = length
        self.modules = {}
        for row in range(self.height):
            for column in range(self.length):
                coordinate = chr(row+65) + str(column+1)
                self.modules.update({coordinate:Module(coordinate)})

    def show(self, owner_perspective = True):
        display_string = ""
        for row in range(self.height + 1):
            for column in range(self.length + 1):
                coordinate = chr(column+64) + str(row)
                module = self.modules.get(coordinate)
                if row == 0 and column == 0:
                    display_string += "   "
                elif row == 0:
                    display_string += chr(column+64) + " "
                elif column == 0:
                    row_num_length = len(str(row))
                    for i in range(2 - row_num_length): display_string += " "
                    display_string += str(row) + " "
                else:
                    if owner_perspective and module.contents != "" and not module.isGuessed: #My board, module contains a ship that hasn't been attacked
                        display_string += module.contents + " "
                    elif owner_perspective and module.contents != "" and module.isGuessed: #My board, module contains a ship that has been attacked
                        display_string += "# "
                    elif owner_perspective and module.contents == "" and not module.isGuessed: #My board, module contains nothing and hasn't been attacked
                        display_string += "~ "
                    elif owner_perspective and module.contents == "" and module.isGuessed: #My board, module contains nothing but has been attacked
                        display_string += "! "                    
                    elif not owner_perspective and module.contents != "" and module.isGuessed: #Enemy board, module contains a ship that has been attacked
                        display_string += "# "
                    elif not owner_perspective and module.contents == "" and module.isGuessed: #Enemy board, module contains nothing and has been attacked
                        display_string += "! "
                    elif not owner_perspective and not module.isGuessed: #Enemy board, default character that masks contents of the module
                        display_string += "~ "
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
        self.is_placed = False

    def __repr__(self):
        return "{name} (Size: {size})".format(name = self.name, size = self.size)