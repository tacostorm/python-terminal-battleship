import battleshipClasses
import os

Board_Length = 10
Board_Height = 10


Default_Ships_P1 = {"Battleship":battleshipClasses.Ship("Battleship", 4), "Carrier":battleshipClasses.Ship("Carrier", 5), "Destroyer":battleshipClasses.Ship("Destroyer", 3), "Submarine":battleshipClasses.Ship("Submarine", 3), "Patrol Boat":battleshipClasses.Ship("Patrol Boat", 2)}
Default_Ships_P2 = {"Battleship":battleshipClasses.Ship("Battleship", 4), "Carrier":battleshipClasses.Ship("Carrier", 5), "Destroyer":battleshipClasses.Ship("Destroyer", 3), "Submarine":battleshipClasses.Ship("Submarine", 3), "Patrol Boat":battleshipClasses.Ship("Patrol Boat", 2)}
One_Ship_P1 = {"Small":battleshipClasses.Ship("Small", 1)}
One_Ship_P2 = {"Small":battleshipClasses.Ship("Small", 1)}
ValidLetters = [chr(i+65) for i in range(Board_Length)]
ValidNumbers = [str(i+1) for i in range(Board_Height)]

def clear_terminal():
    os.system('cls')

def is_ship_selection_valid(player, input):
    found = False
    for i in player.ships:
        if i[0] == input:
            found = True
    return found

def is_coordinate_selection_valid(input):
    #so we exepct input in the form of LETTER + NUMBER, maximum of 3 character (A10)
    #We should expect up to 26x26 grids, so Z26 is theoretically the highest we want to support
    valid = False
    valid = input[0] in ValidLetters and input[1:] in ValidNumbers
    return valid

def is_coordinate_already_guessed(input, enemy):
    return enemy.play_area.modules[input].isGuessed 

def render_ui(player, enemy, show_ships = False, show_player_board = True, show_enemy_board = False):
    clear_terminal()
    print("Player {num}'s Turn!".format(num = player.id))
    if show_ships:
        print("Your Ships Available to Place\n")
        for i in player.ships:
            if not player.ships[i].is_placed: print(player.ships[i])
        print("\n")
    if show_player_board:
        print("Your Play Area")
        print("\n" + player.play_area.show())
    if show_enemy_board:
        print("Enemy's Play Area")
        print("\n" + enemy.play_area.show(False))
    pass

#Function to clear the screen and allow the next player to start their turn when ready.
def switch_player():
    pass

#I assume there's a way to refactor this, since I'm essentially running two functions 4 times each.
def get_valid_ship_orientations(modules, ship_size, coordinate):
    valid_orientations = {"Up": True, "Down": True, "Left": True, "Right": True}
    column = coordinate[0]
    row = coordinate[1:]
    coordinates = []
    for i in range(1, ship_size):
        #Check Up orientation
        coordinate_to_test = column + str(int(row)-i)
        coordinates.append(coordinate_to_test)
        if modules.get(coordinate_to_test) == None or modules[coordinate_to_test].contents != "": 
            valid_orientations.update({"Up":False})
    valid_orientations.update({"Up": [valid_orientations["Up"], coordinates]})
    coordinates = []
    for i in range(1, ship_size):
        #Check Down orientation
        coordinate_to_test = column + str(int(row)+i)
        coordinates.append(coordinate_to_test)
        if modules.get(coordinate_to_test) == None or modules[coordinate_to_test].contents != "": 
            valid_orientations.update({"Down":False})
    valid_orientations.update({"Down": [valid_orientations["Down"], coordinates]})
    coordinates = []
    for i in range(1, ship_size):
        #Check Left orientation
        coordinate_to_test = chr(ord(column)-i) + row
        coordinates.append(coordinate_to_test)
        if modules.get(coordinate_to_test) == None or modules[coordinate_to_test].contents != "": 
            valid_orientations.update({"Left":False})
    valid_orientations.update({"Left": [valid_orientations["Left"], coordinates]})
    coordinates = []
    for i in range(1, ship_size):
        #Check Right orientation
        coordinate_to_test = chr(ord(column)+i) + row
        coordinates.append(coordinate_to_test)        
        if modules.get(coordinate_to_test) == None or modules[coordinate_to_test].contents != "": 
            valid_orientations.update({"Right":False})
    valid_orientations.update({"Right": [valid_orientations["Right"], coordinates]})
    if not valid_orientations["Up"][0]: valid_orientations.pop("Up")
    if not valid_orientations["Down"][0]: valid_orientations.pop("Down")
    if not valid_orientations["Left"][0]: valid_orientations.pop("Left")
    if not valid_orientations["Right"][0]: valid_orientations.pop("Right")
    return valid_orientations

def placement_phase(active_player, enemy):
    while active_player.get_number_unplaced_ships() > 0:
        #Selecting a ship to place flow
        render_ui(active_player, enemy,True,True)
        print("Please enter the first letter of the ship you'd like to place: ")
        selection = input()
        while not is_ship_selection_valid(active_player, selection):
            render_ui(active_player, enemy,True,True)
            print("{ship} is invalid. Please enter the first letter of the ship you'd like to place: ".format(ship = ship))
            selection = input()
        ship = active_player.get_ship_from_input(selection)

        #Selecting a coordinate to place the ship
        render_ui(active_player, enemy,True,True)
        print("Enter the coordinate for one end of your ship (E.G. E4): ")
        starting_coordinate = input()
        while not is_coordinate_selection_valid(starting_coordinate) or active_player.play_area.modules[starting_coordinate].contents != "":
            render_ui(active_player, enemy,True,True)
            print("{coord} is not valid. Please enter a valid coordinate: ".format(coord=starting_coordinate))
            starting_coordinate = input()

        #Placing an orientation for the ship
        render_ui(active_player, enemy,True,True)
        valid_orientations = get_valid_ship_orientations(active_player.play_area.modules, active_player.ships[ship].size, starting_coordinate)
        valid_directions = ""
        for i in valid_orientations.keys():
            valid_directions += i + " "
        print("Valid Directions: {directions} ".format(directions = valid_directions))
        print("Which direction should the ship go from {coordinate}: ".format(coordinate = starting_coordinate))
        direction = input()
        while not direction in valid_orientations.keys():
            render_ui(active_player, enemy,True,True)
            print("Valid Directions: {directions} ".format(directions = valid_directions))
            print("{direction} is not a valid direction. Please enter a valid direction: ".format(direction = direction))
            direction = input()

        #Putting the ship on the board
        coordinates_for_ship = valid_orientations[direction][1]
        coordinates_for_ship.append(starting_coordinate)
        active_player.place_ship(coordinates_for_ship, ship)
        render_ui(active_player, enemy,True,True)

def main_game_loop(player_1, player_2):
    active_player = player_1
    enemy = player_2
    while player_1.is_alive() and player_2.is_alive():
        render_ui(active_player, enemy, False, True, True)
        print("What coordinate will you target (E.G. E4):")
        target = input()
        while not is_coordinate_selection_valid(target) or is_coordinate_already_guessed(target, enemy):
            render_ui(active_player, enemy, False, True, True)
            print("{coord} is not valid or already targeted. Please enter a valid coordinate: ".format(coord=target))
            target = input()
        result = active_player.attacks(enemy, target)
        render_ui(active_player, enemy, False, True, True)
        print("{target} is a {result}".format(target = target, result = result))
        print("Press enter to clear your screen ")
        input()
        clear_terminal()
        print("Press enter when Player {id} is ready!".format(id = enemy.id))
        input()
        original_active_player = active_player 
        active_player = enemy
        enemy = original_active_player
    if player_1.is_alive():
        return player_1
    else:
        return player_2
    pass

def victory_screen(winner):
    clear_terminal()
    print("The winner is Player {id}".format(id = winner.id))
    pass

def intro_screen():
    pass

#One version for Testing    
#player_list =[battleshipClasses.Player(One_Ship_P1, Board_Height, Board_Length), battleshipClasses.Player(One_Ship_P2, Board_Height, Board_Length)]
#One version for the real game
player_list =[battleshipClasses.Player(Default_Ships_P1, Board_Height, Board_Length), battleshipClasses.Player(Default_Ships_P2, Board_Height, Board_Length)]


placement_phase(player_list[0], player_list[1])
placement_phase(player_list[1], player_list[0])
winner = main_game_loop(player_list[0], player_list[1])
victory_screen(winner)



