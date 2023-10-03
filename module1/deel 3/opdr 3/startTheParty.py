gastheer = False
gasten = True
drank = True
chips = False

if (gasten or gastheer) and (chips and drank or gastheer and not chips) and (gasten or chips or drank):
    print('Start the Party')
else:
    print('No Party')
