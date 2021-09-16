from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
amount = 11
for i in range(5):
    amount = amount - 2
    robotArm.grab()
    for g in range(0,amount):
        robotArm.moveRight()
    robotArm.drop()
    for g in range(0,amount -1):
        robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()