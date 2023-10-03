gastheer = input("Wie is de gastheer?")
drank = True
chips = False
party = False

if gastheer == 'nevin':
    gasten = int(input('Hoeveel gasten zijn er?'))
    
    if gasten > 3 and gasten < 21:
        if (gasten or gastheer) and (chips and drank or gastheer and not chips) and (gasten or chips or drank):
            party = True

if party:
    print("Party Started")
else:
    print('No Party')