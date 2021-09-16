from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for g in range(9):
    robotArm.moveRight()

for i in range(9):
    robotArm.moveLeft()
    for c in range(1):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()