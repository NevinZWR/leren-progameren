from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
for i in range(5):
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    if i <= 3:
        robotArm.moveRight()
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()