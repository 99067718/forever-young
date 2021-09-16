from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5

for i in range(10):
    robotArm.moveRight()
for c in range(4):
    robotArm.moveLeft()
    robotArm.moveLeft()
    for g in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

for i in range(10):
    robotArm.moveRight()
for p in range(6):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
        




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()