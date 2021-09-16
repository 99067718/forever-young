from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for i in range(4):
    robotArm.moveLeft()
for c in range(2):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
    robotArm.grab
robotArm.moveRight()
for c in range(3):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
    robotArm.grab

robotArm.moveRight()
for c in range(4):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
    robotArm.grab





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()