from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
move = 0
move +=1
while True:
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for i in range(move):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(move):
            robotArm.moveLeft()
        move +=1

    else:
        break         

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()