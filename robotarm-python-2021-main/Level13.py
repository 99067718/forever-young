from pygame import Color
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
hasBlock = True
moves = 0
while hasBlock == True:
    moves = moves + 1
    robotArm.grab()
    Color = robotArm.scan()
    if Color == "":
        print("There are no blocks left")
        break
    for c in range(0,moves,1):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(0,moves,1):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()