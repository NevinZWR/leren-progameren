from collections import Counter
from youhadonejob import *
import math, random

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    # Gemiddelde berekenen
    aantal = aantalgetal(getallen)

    # Som van alle getallen in de lijst
    som = bereken_som(getallen)

    # Gemiddelde berekenen
    gemiddelde = bereken_gem(getallen)

    # Het grootste getal in de lijst
    grootste_getal = grootgetal(getallen)
    
    # Het kleinste getal in de lijst
    kleinste_getal = kleingetal(getallen)
    
    # Het eerste getal in de lijst
    eerste_getal = eerstegetal(getallen)
    
    # Het kleinste getal gedeeld door het eerste controle getal
    delen1 = deelgetal(getallen, controlegetal1)

    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = deelgetal2(getallen, controlegetal2)

    # alle unieke getallen
    unieke_getallen = uniekgetal(getallen)

    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = uniekelementen(getallen)

    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil1 = verschil(getallen, controlegetal1)

    # Sorteer de lijst van getallen
    gesorteerde_lijst = sorteerlijst(getallen)

    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = sorted(unieke_getallen)

    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    telling_elementen = tel_elementen(getallen)

    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = deelbaren(unieke_getallen, controlegetal1)

    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = deelbaren2(unieke_getallen, controlegetal2)

    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = komtvoren(getallen, controlegetal1, controlegetal2)

    # Vindt de posities van heteerste controle getal
    posities = vind_posities(getallen, controlegetal1)
    
    # Standaardafwijking berekenen
    standaardafwijking = bereken_standaardafwijking(getallen)

    # Shuffle de lijst
    shufflelijst(getallen)

    # Pak een random getal uit de lijst
    random_getal =  randomgetal(getallen)

    # Verschil tussen twee getallen
    verschil2 = vershillen2(random_getal, controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")