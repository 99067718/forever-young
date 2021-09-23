from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
NmmrOfMoves = 0
for i in range(4):
    NmmrOfMoves = NmmrOfMoves + 1
    for c in range(0,NmmrOfMoves,1):
        robotArm.grab()
        for g in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for g in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()







# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()