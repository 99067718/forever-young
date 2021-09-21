from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
moves = 9
for i in range(9):
    moves = moves - 1
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for c in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for g in range(0,moves,1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()