import battleshipClasses

DefaultShips = [battleshipClasses.Ship("Battleship", 4),battleshipClasses.Ship("Carrier", 5), battleshipClasses.Ship("Destroyer", 3), battleshipClasses.Ship("Submarine", 3), battleshipClasses.Ship("Patrol Boat", 2)]
ShipsDict = {"Battleship":4, "Carrier":5, "Destroyer":3, "Submarine":3, "Patrol Boat":2}


test = battleshipClasses.PlayArea(10,10)
print(test.show())

