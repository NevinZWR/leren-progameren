from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
move = 9
for _ in range(move):
    print(move)
    robotArm.grab()
    color = robotArm.scan()
    if color == "red": 
        for _ in range(move):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(move-1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    move -=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()