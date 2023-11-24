import time
import sys


def slowprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02) 


slowprint("Hallo, Welkom bij het spel de Spokerige Escaperoom van Heracles\n")
slowprint("In dit spel kan u keuzes maken en elke keuze brengt een ander einde\n")

while True:
    start_game = input("Wilt u beginnen? ")

    if start_game.lower() == "ja":
        slowprint("Veel succes\n")
        break 
    elif start_game.lower() == "nee":
        print('''
███████████████████████████████████████████████████████▀█████████████████████████████████████████████████████
█─▄─▄─█─▄▄─█─▄─▄─███▄─▄▄▀█▄─▄▄─███▄─█─▄█─▄▄─█▄─▄███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█▄─▄▄─███▄─█─▄█▄─▄▄─█▄─▄▄─█▄─▄▄▀█
███─███─██─███─██████─██─██─▄█▀████▄▀▄██─██─██─██▀█─██▄─██─▄█▀██─█▄▀─███─██─██─▄█▀████─▄▀███─▄█▀██─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▀▀▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

        ''')
        break
    else:
        print("Ongeldige invoer. Voer 'ja' of 'nee' in.")

if start_game.lower() == "ja":
    slowprint("Jij en je vriend Joes zijn terecht gekomen in de Spokerige Escaperoom van Heracles. Jullie hebben een keuze tussen 2 deuren. Welke kies je?")
    slowprint('''
    Optie A Rechter deur
    Optie B Linker deur
    Optie C Ren weg\n''')
    eerste_vraag = input("U kiest voor Optie ")

    if eerste_vraag == "A":
        slowprint("Jij en Joes zijn terecht gekomen in een kamer met twee deuren die langzaam dichtgaan. Jullie zien achterin de kamer een deur, wat gaan jullie doen?")
        slowprint('''
    Optie A Jullie zoeken naar de sleutel
    Optie B Jullie proberen de deur in te trappen
    Optie C Je wacht\n''')
        rechterdeur_vraag1 = input("U kiest voor Optie ")

        if rechterdeur_vraag1 == "A":
            slowprint("Jullie vinden de sleutel net op tijd en komen levend de kamer uit, maar nu zie je 2 glijbanen")
            slowprint('''
    Optie A Neem de linker glijbaan
    Optie B Neem de rechter glijbaan\n''')
            rechterdeur_vraag2 = input("U kiest voor Optie ")

            if rechterdeur_vraag2 == "A":
                slowprint("jullie gaan van de glijbaan af met 90 km/h en knalt tegen een muur aan")
                print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
            elif rechterdeur_vraag2 == "B":
                slowprint("jullie glijden met 30 km/h per uur de glijbaan af en jullie belanden in een verlaten waterpark, alle deuren en ramen zitten opslot het waterstijgt langzaam omhoog en er staat een timer van 2 uur, wat ga je doen om hier uit te komen")
                slowprint('''
    Optie A je probeerd het raam te breken
    Optie B je zoekt een uitgang\n''')
                rechterdeur_vraag3 = input("U kiest voor Optie ")
        if rechterdeur_vraag3 == "A":
                slowprint("Je probeerde het raam te breken met je ring, dit lukte jullie zijn nu buiten en zijn vrij")
                print('''
                █▄█ █▀█ █░█   █░█░█ █ █▄░█
                ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
        elif rechterdeur_vraag3 == "B":
                slowprint("Jullie hebt het hele zwembad afgezocht en uiteindelijk toen het bijna was volgelopen was zijn jullie via het dak ontsnapt uit het zwembad jullie zijn nu door het dak aan het kruipen maar BOEM... het dakt zakt in en jullie belanden in de volgende kamer de kamer is helemaal leeg maar en hangen 2 knoppen aan de muur rood en blauw welke druk je in") 
                slowprint('''
    Optie A druk de blauwe knop in
    Optie B druk de rode knop in\n''')
                rechterdeur_vraag4 = input("U kiest voor Optie ")
                if rechterdeur_vraag4 == "A":
                    slowprint("KABOEM!    confetti")
                    print('''
                █▄█ █▀█ █░█   █░█░█ █ █▄░█
                ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
                elif rechterdeur_vraag4 == "B":
                    slowprint("KABOEM! er ontploft dynamite en jullie gaan ten onderen")   
                    print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')            





        elif rechterdeur_vraag1 == "B":
            slowprint("Jullie proberen de deur in te trappen, maar het lukt niet. Jullie worden opgesloten.")
            print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
        elif rechterdeur_vraag1 == "C":
            slowprint("Jullie wachten... en er gebeurt niets.")
            print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')


    elif eerste_vraag == "B":
        slowprint("Jullie komen in een kamer en zien een dode man. Jullie proberen terug te gaan maar de deur was dicht gevallen jullie zien een deur in de hoek van de kamer, maar wat gaan jullie doen")
        slowprint('''
    Optie A zoek naar een sleutel
    Optie B kruip in de luchtschaft
    Optie C verstop je in de kamer\n''')
        linkerdeurvraag1 = input("U kiest voor Optie ")
        if linkerdeurvraag1 == "A":
            slowprint("jullie vinden de sleutel maar wat raar hij opent de deur niet, jullie zoeken naar wat de zleutel wel kan openen en jullie zien oppeens een luik richting een kelder met de sleutel zijn jullie in de kelder gekomen in de kelder zitten heel veel ratten maar is wel een trap naar boven. Jullie gaan naar boven en jullie zijn in een nieuwe kamer hier zijn er twee trappen eentje is rood en eentje is blauw")
            slowprint('''
    Optie A Neem de blauwe trap
    Optie B Neem de rode trap \n''')           
        if linkerdeurvraag1 == "B":
            slowprint()
            slowprint('''
    Optie A 
    Optie B \n''')
        if linkerdeurvraag1 == "C":
            slowprint("Jullie zitten verstopt en er komt iemand met een masker binnen gelopen hij gooit een gas bom in de kamer en jullie stikken")
            print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')        


    elif eerste_vraag == "C":
        slowprint("jullie proberen weg te rennen maar worden gepakt door de geesten")
        print('''
█▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
