from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 1
for x in range(8):
    robotArm.moveRight()
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if i < 8:
        robotArm.moveLeft()
robotArm.wait()