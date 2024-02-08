import sys

def exit_program():
    print("eind")
    sys.exit(0)
PRIJS_COLA = 1.99
PRIJS_BIER = 2.49
PRIJS_CHAMPAGNE = 12.49

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

leeftijd = int(input("Hoe oud ben je? "))
overhvljaar = 18 - leeftijd
overhvljaar2 = 21 - leeftijd
kleurband = "blauw"
vip = "nee"
if leeftijd < 18:
    print("Sorry, je mag niet naar binnen")
    print(f"Probeer over {overhvljaar} jaar nog eens")
    exit_program()
else:
    naam = input("Wat is je naam? ").lower()
    if naam in VIP_LIST: 
       vip = "ja"
    if vip == "ja":
        if leeftijd < 21:
            kleurband = "rood"
            print(f"Je krijgt van mij een {kleurband} bandje")
        else:
            print(f"Je krijgt van mij een {kleurband} bandje")
    if vip == "nee":
        if leeftijd >= 21:       
            print("Je krijgt een stempel van mij")
    if vip == "ja":
        leeftijd = 21
print("Wat wil je drinken? ")

drank = input("Kies uit Cola, Bier en Champagne: ").lower()

if drank == "cola":
    if vip == "ja":
        print("Astublieft, complimenten van het huis")
    else:
        print(f"Alsjeblieft, je cola kost {PRIJS_COLA}")
elif drank == "bier":
    if leeftijd >= 21:
        if vip == "ja":
            print("Astublieft, complimenten van het huis")
        else:
            print(f"Alsjeblieft, je bier kost {PRIJS_BIER}")
    else:
        print("Sorry, je mag nog geen alcohol bestellen onder de 21")
        print(f"Probeer het over {overhvljaar2} jaar nog eens")
elif drank == "champagne":
    if vip == "ja":
        if leeftijd >= 21:
            print(f"Alsjeblieft, je champagne kost {PRIJS_CHAMPAGNE}")
            
        else:
            print("Sorry, je mag nog geen alcohol bestellen onder de 21")
            print(f"Probeer het over {overhvljaar2} jaar nog eens")
    else:
        print("alleen vips mogen champagne bestellen")        
else:
    print("Sorry, we hebben dat hier niet. Hier is een glaasje water.")
