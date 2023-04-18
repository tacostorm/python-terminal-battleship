import battleshipClasses

Two_Ships_P1 = {"Small":battleshipClasses.Ship("Small", 2), "Medium":battleshipClasses.Ship("Medium",3)}
Two_Ships_P2 = {"Small":battleshipClasses.Ship("Small", 2), "Medium":battleshipClasses.Ship("Medium",3)}

print("""This will execute a bunch of tests for all the class methods
If everything is true, then tests all pass!\n""")

#Player Tests
#test __init__
#test __repr__
player1 = battleshipClasses.Player(Two_Ships_P1,3,3)
player2 = battleshipClasses.Player(Two_Ships_P2,3,3)
print("Testing Player Class")
print(player1.id == 1)
print(player2.id == 2)
print(player1.max_health == 5)
print(player2.max_health == 5)
player1.place_ship(["A1", "A2", "A3"], "Small")
print(player1.is_ship_selection_valid("S"))
print(player1.is_ship_selection_valid("s"))
print(player1.get_number_unplaced_ships() == 1)
print(player2.get_number_unplaced_ships() == 2)
print(player1.get_ship_from_input("S") == "Small")
print(player1.get_ship_from_input("s") == "Small")
print(player1.is_alive() == True)
print(player2.attacks(player1, "A1") == "hit!")
print(player2.attacks(player1, "a2") == "hit!") 
print(player2.attacks(player1, "C1") == "miss.")
print(player1.get_health() == 3)
player1.health = 0
print(player1.is_alive() == False)


#print(get_valid_ship_orientations(player1.play_area.modules, 4, "E3"))

#Play Area Tests
#test __init__
#test __repr__

#Module Tests
print("\nBeginning Module Class Tests")
test_module = battleshipClasses.Module("A2", "Battleship", True)
print(test_module.contents == "Battleship")
print(test_module.coordinates == "A2")
print(test_module.isGuessed == True)
#test __repr_

#Ship Tests
print("\nBeginning Ship Class Tests")

print(str(player1.ships["Small"]) == "Small (Size: 2)")
print(player1.ships["Small"].is_placed)
print(player1.ships["Small"].name == "Small")
print(player1.ships["Small"].size == 2)