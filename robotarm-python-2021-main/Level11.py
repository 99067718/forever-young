from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    print(color)
    if color == "white":
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()
        color2 = robotArm.scan()
        if color2 == "white":
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
            robotArm.grab()
            color3 = robotArm.scan()
            if color3 == "white":
                robotArm.moveRight()
                robotArm.moveRight()
                robotArm.drop()
                robotArm.moveLeft()
                robotArm.grab()
                color4 = robotArm.scan()
                if color4 == "white":
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    exit

        else:
            robotArm.drop()
            robotArm.moveRight()
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
            robotArm.moveRight()

    
    else:robotArm.drop()
    robotArm.moveRight()
    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()