from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 0.1
# Jouw python instructies zet je vanaf hier:
for i in range(10):
    robotArm.grab()
    for x in range(5):
        robotArm.moveRight()
    robotArm.drop()
    if i == 0 or i == 2 or i == 5:
        aantal = 4
    else:
        aantal = 5
    for y in range(aantal):
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()