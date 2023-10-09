OPTIES = ["altijd 0", "vaak 1", "regelmatig 2", "soms 3", "nooit 4"]
COMPETENTIE_ADVIES_ZORGELIJK = "Zorgelijk advies"
COMPETENTIE_ADVIES_TWIJFELACHTIG = "Twijfelachtig advies"
COMPETENTIE_ADVIES_GERUSTSTELLEND = "Geruststellend advies"
STUDIEDOKTER_TITEL = "Welkom bij de Studiedokter!"
AANTAL_WEKEN_VRAAG = "Hoeveel weken heb je gestudeerd? "

def vraag_antwoord(stelling):
    print(stelling)
    print(OPTIES)
    antwoord = int(input("Kies het passende nummer (0-4): "))
    return antwoord

def bepaal_advies(antwoorden):
    gemiddelde_score = sum(antwoorden) / len(antwoorden)
    aantal_altijd = antwoorden.count(0)
    aantal_vaak = antwoorden.count(1)
    aantal_regelmatig = antwoorden.count(2)
    
    if gemiddelde_score <= 2 or (aantal_altijd + aantal_vaak) > len(antwoorden) / 2:
        return COMPETENTIE_ADVIES_ZORGELIJK
    elif gemiddelde_score <= 3 or (aantal_altijd + aantal_vaak + aantal_regelmatig) > len(antwoorden) / 2:
        return COMPETENTIE_ADVIES_TWIJFELACHTIG
    else:
        return COMPETENTIE_ADVIES_GERUSTSTELLEND
    
print(STUDIEDOKTER_TITEL)
weken = int(input(AANTAL_WEKEN_VRAAG))

antwoorden = []
for i in range(7):
    stelling = f"Beoordeel competentiestelling {i+1}:"
    antwoord = vraag_antwoord(stelling)
    antwoorden.append(antwoord)

advies = bepaal_advies(antwoorden)
print("Resultaat:")
print(advies)
