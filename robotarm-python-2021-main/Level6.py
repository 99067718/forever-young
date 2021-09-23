from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for g in range(8):
    robotArm.moveRight()

for i in range(8):
    robotArm.moveLeft()
    
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()