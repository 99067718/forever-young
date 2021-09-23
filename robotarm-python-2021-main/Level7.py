from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2

for i in range(9):
    robotArm.moveRight()
for c in range(5):  
    for g in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveLeft()
    robotArm.moveLeft()

        




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()