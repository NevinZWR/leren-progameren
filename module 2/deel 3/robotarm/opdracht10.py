from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 1
# Jouw python instructies zet je vanaf hier:
aantal = 9
for i in range(5):
    robotArm.grab()
    for x in range(aantal):
        robotArm.moveRight()
    aantal -= 1 
    robotArm.drop()
    for j in range(aantal):
        robotArm.moveLeft()
    aantal -= 1




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()