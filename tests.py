import battleshipClasses

print("""This will execute a bunch of tests for all the class methods
If everything is true, then tests all pass!""")

#Player Tests
#test __init__
#test __repr__

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
test_ship = battleshipClasses.Ship("Test", 5)
print(test_ship.name == "Test")
print(test_ship.size == 5)
print(str(test_ship) == "Test of size 5")