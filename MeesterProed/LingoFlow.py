import random
from FunctiesLingo import *
from DataLingo import *

# Hoofdprogramma
while True:
    woord = selecteer_woord()
    print(woord)
    pogingen = 5
    feedback = toon_beginletter(woord) + "_" * (len(woord) - 1)
    correcte_pogingen = 0
    rode_ballen = 0
    groene_ballen = 0
    bingokaart = [["_" for _ in range(4)] for _ in range(4)]

    print(f"Welkom bij Lingo! Raad het woord dat begint met '{feedback[0]}'.")

    while pogingen > 0:
        poging = nieuwe_poging(woord, feedback)
        feedback = controleer_poging(woord, poging)
        print("Feedback:", feedback)

        if feedback.replace(KLEUR_GROEN, '').replace(KLEUR_RESET, '').upper() == woord:
            print("Correct geraden!")
            correcte_pogingen += 1

            bal1, bal2 = grabbelen()
            print(f"Je hebt de ballen '{bal1}' en '{bal2}' gegrabbeld.")

            if bal1 == "Rood" or bal2 == "Rood":
                rode_ballen += 1
                if rode_ballen >= 3:
                    print("3 rode ballen getrokken. Spel afgelopen.")
                    break
            if bal1 == "Groen":
                groene_ballen += 1
            if bal2 == "Groen":
                groene_ballen += 1

            bingokaart = update_bingokaart(bingokaart, bal1)
            if bal1 != "Rood":  # Controleer alleen de tweede bal als de eerste geen rode bal is
                bingokaart = update_bingokaart(bingokaart, bal2)

            print_bingokaart(bingokaart)

            if controleer_bingo(bingokaart):
                print("Bingo! Gefeliciteerd, je hebt gewonnen!")
                break

            if groene_ballen >= 3:
                print("3 groene ballen getrokken. Gefeliciteerd, je hebt gewonnen!")
                break

            pogingen = 5
            woord = selecteer_woord()
            feedback = toon_beginletter(woord) + "_" * (len(woord) - 1)
            print(f"Nieuw woord: {feedback[0]}")
        else:
            pogingen -= 1
            if pogingen == 0:
                print("Geen pogingen meer over. Spel afgelopen.")
            elif pogingen == 1:
                print(f"Nog 1 poging over.")
            else:
                print(f"Nog {pogingen} pogingen over.")
    
    nog_een_keer = input("Wil je nog een keer spelen? (ja/nee): ").lower()
    if nog_een_keer == "ja":
        pass
    else:
        print("Bedankt voor het spelen!")
        break
