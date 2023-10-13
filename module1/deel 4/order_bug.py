
def vraag_getal(aantal):
    antwoord = input("Voer het "+antwoord+" getal in: ")
    getal = int(aantal)
    return getal

getal_1 = int(input("wat is het eerste getal "))
getal_2 = int(input("wat is het tweede getal "))


if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = (getal_1 / getal_2)
    print ("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))
    

def deel_getallen(a, b):
    return (a , b)