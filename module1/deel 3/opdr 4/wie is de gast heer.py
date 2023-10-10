gastheer = input("Wie is de gastheer?")
gasten = True
drank = True
chips = False


if gastheer == "nevin":
    print('Start the Party')
elif gastheer == "wilfred":
    print('No Party')
else:

    if (gasten or gastheer) and (chips and drank or gastheer and not chips) and (gasten or chips or drank):
        print('Start the Party')
    else:
        print('No Party')