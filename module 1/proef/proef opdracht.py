import time
import sys

def slowprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

slowprint("Hallo, Welkom bij het spel de Spokerige Escaperoom van Heracles\n")
slowprint("In dit spel kun je keuzes maken en elke keuze brengt een ander einde\n")

while True:
    start_game = input("Wil je beginnen? ")

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
    eerste_vraag = input("Je kiest voor Optie ")

    if eerste_vraag == "A":
        slowprint("Jij en Joes zijn terecht gekomen in een kamer met twee deuren die langzaam dichtgaan. Jullie zien achterin de kamer een deur, wat gaan jullie doen?")
        slowprint('''
    Optie A Jullie zoeken naar de sleutel
    Optie B Jullie proberen de deur in te trappen
    Optie C Je wacht\n''')
        rechterdeur_vraag1 = input("Je kiest voor Optie ")

        if rechterdeur_vraag1 == "A":
            slowprint("Jullie vinden de sleutel net op tijd en komen levend de kamer uit, maar nu zie je 2 glijbanen")
            slowprint('''
    Optie A Neem de linker glijbaan
    Optie B Neem de rechter glijbaan\n''')
            rechterdeur_vraag2 = input("Je kiest voor Optie ")

            if rechterdeur_vraag2 == "A":
                slowprint("Jullie gaan van de glijbaan af met 90 km/h en knallen tegen een muur")
                print('''
                        █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                        ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
            elif rechterdeur_vraag2 == "B":
                slowprint("Jullie glijden met 30 km/h per uur de glijbaan af en belanden in een verlaten waterpark. Alle deuren en ramen zitten op slot en het water stijgt langzaam omhoog. Er staat een timer van 2 uur. Wat ga je doen om hier uit te komen?")
                slowprint('''
    Optie A Je probeert het raam te breken
    Optie B Je zoekt een uitgang\n''')
                rechterdeur_vraag3 = input("Je kiest voor Optie ")

                if rechterdeur_vraag3 == "A":
                    slowprint("Je probeert het raam te breken met je ring. Dit lukt en jullie zijn nu buiten en vrij.")
                    print('''
                    █▄█ █▀█ █░█   █░█░█ █ █▄░█
                    ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
                elif rechterdeur_vraag3 == "B":
                    slowprint("Jullie hebben het hele zwembad afgezocht en uiteindelijk, toen het bijna was volgelopen, zijn jullie via het dak ontsnapt uit het zwembad. Jullie kruipen door het dak, maar BOEM... het dak zakt in en jullie belanden in de volgende kamer. De kamer is helemaal leeg, maar er hangen 2 knoppen aan de muur: rood en blauw. Welke druk je in?")
                    slowprint('''
    Optie A Druk op de blauwe knop
    Optie B Druk op de rode knop\n''')
                    rechterdeur_vraag4 = input("Je kiest voor Optie ")
                    if rechterdeur_vraag4 == "A":
                        slowprint("KABOEM! Confetti")
                        print('''
                        █▄█ █▀█ █░█   █░█░█ █ █▄░█
                        ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
                    elif rechterdeur_vraag4 == "B":
                        slowprint("KABOEM! Er ontploft dynamiet en jullie gaan ten onder")
                        print('''
                        █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                        ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')

        elif rechterdeur_vraag1 == "B":
            slowprint("Jullie proberen de deur in te trappen, maar het lukt niet. Jullie worden opgesloten.")
            print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
        elif rechterdeur_vraag1 == "C":
            slowprint("Jullie wachten... en er gebeurt niets, en je word plat gedrukt door de muuren")
            print('''
                █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
                ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')

    elif eerste_vraag == "B":
        slowprint("Jullie komen in een kamer en zien een dode man. Jullie proberen terug te gaan maar de deur was dichtgevallen. Jullie zien een deur in de hoek van de kamer, maar wat gaan jullie doen?")
        slowprint('''
    Optie A Zoek naar een sleutel
    Optie B Kruip in de luchtschacht
    Optie C Verstop je in de kamer\n''')
        linkerdeurvraag1 = input("Je kiest voor Optie ")
        if linkerdeurvraag1 == "A":
            slowprint("Jullie vinden de sleutel maar wacht is... deze opent de deur niet jullie zien een kelder en deze opent de sleutel wel jullie komen terecht in een donkere kelder... BOEM de kelder valt dicht, Hoe gaan jullie uit de kelder komen?")
            slowprint('''
    Optie A verstop je in de donkere kamer
    Optie B zoek naar een uitgang\n''')
            linkerdeurvraag2 = input("Je kiest voor Optie ")
            if linkerdeurvraag2 == "A":
                slowprint("Jullie verstoppen jezelf in de donkere kamer, ... het was lang stil en oppeens BOEM er werd een granaat naar binnen geworpen.")
                print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
            elif linkerdeurvraag2 == "B":
                slowprint("Jullie zoeken naar een uitgang maar het is donker dus jullie kunnen niet goed zien, na even zoeken vinden jullie een trap naar boven in deze kamer bevind zich 2 ladders eentje is blauw en de andere is rood welke nemen jullie(er is geen weg terug!)")
                slowprint('''
    Optie A Jullie nemen de blauwe ladder
    Optie B Jullie nemen de rode ladder\n''')
                linkerdeurvraag3 = input("Je kiest voor Optie ")
                if linkerdeurvraag3 == "A":
                    slowprint("jullie klimmen naar boven en komen terecht in een garage jullie zien een auto en besleuten de garage deur open te rammen nu zijn jullie vrij")
                    print('''
                        █▄█ █▀█ █░█   █░█░█ █ █▄░█
                        ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
                elif linkerdeurvraag3 == "B":
                    slowprint("Jullie klimmen naar boven en komen terecht in een dichte kamer en er is geen manier om hier uit te komen, jullie verhongeren")
                    print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
        elif linkerdeurvraag1 == "B":
            slowprint("Jullie kruipen door de luchtschacht en oppeens.... PAF jullie vallen naar beneden jullie komen in een kamer terecht, in deze kamer zit sietze hij neemt onderdeel in jullie avondtuur. in deze kamer zit ook een open deur. maar gaan jullie erin")
            slowprint('''
    Optie A Jullie gaan door de deur
    Optie B Jullie wachten\n''')
            linkerdeurvraag4 = input("Je kiest voor Optie")
            if linkerdeurvraag4 == "A":
                slowprint("jullie openen de deur dit zetten een boobietrap af en sietze word geraakt door een peil, sietze overlijd in veel pein maar jullie kunnen door gaan, jullie zitten nu in een kamer met sleutels en 2 deuren(links en rechts) welke deur openen jullie")
                slowprint('''
    Optie A Open de linker deur
    Optie B Open de rechter deu\n''')
                linkerdeurvraag5 = input("Je kiest voor Optie ")
                if linkerdeurvraag5 == "A":
                    slowprint("Jullie openen de linker deur hier zaten 100 giftige slangen die jullie aanvallen")
                print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')  
                if linkerdeurvraag5 == "B":
                    slowprint("Jullie openen de rechter deur deze brengt jullie naar buiten")
                    print('''
                        █▄█ █▀█ █░█   █░█░█ █ █▄░█
                        ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')    
            elif linkerdeurvraag4 == "B":
                slowprint("Jullie wachten in de kamer en oppeens komt er een geest binnen deze griezeld jullie voor de rest van jullie leven ")
                print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')             
    elif eerste_vraag == "C":
        slowprint("Jullie proberen weg te rennen maar worden gepakt door de geesten")
        print('''
            █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
            ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄''')
