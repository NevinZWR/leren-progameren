import math, random

def aantalgetal(getallen:list):
    aantalgetallen = len(getallen)
    return aantalgetallen


def bereken_som(getallen:list):
    som = sum(getallen)
    return som

def bereken_gem(getallen:list):
    som = sum(getallen)
    aantal = len(getallen)
    gemiddelde = som / aantal
    return gemiddelde

def grootgetal(getallen:list):
    grtgetal = max(getallen)
    return grtgetal

def kleingetal(getallen:list):
    mingetal = min(getallen)
    return mingetal

def eerstegetal(getallen:list):
    eerste_getal = getallen[0]
    return eerste_getal

def deelgetal(getallen:list, controleGetal:int):
    delengetal = min(getallen) / controleGetal
    return delengetal

def deelgetal2(getallen:list, controleGetal2:int):
    delengetal2 = max(getallen) / controleGetal2
    return delengetal2

def uniekgetal(getallen:list):
    uniekegetal = list(set(getallen))
    return uniekegetal

def uniekelementen(getallen:list):
    uniekegetal = list(set(getallen))
    uniekelement = len(uniekegetal)
    return uniekelement

def verschil(getallen, controleGetal3):
    uniekegetal = list(set(getallen))
    uniekelement = len(uniekegetal)
    verschillen = abs(uniekelement - controleGetal3)
    return verschillen

def sorteerlijst(getallen:list):
    sortedgetal = sorted(getallen)
    return sortedgetal

def tel_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal] + 1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

def deelbaren(unieke_getallen, controleGetal1):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controleGetal1 == 0:
            deelbaar1.append(getal)
    deelbaren1 = sorted(deelbaar1)
    return deelbaren1

def deelbaren2(unieke_getallen, controleGetal2):
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controleGetal2 == 0:
            deelbaar2.append(getal)
    deelbaren2 = sorted(deelbaar2)
    return deelbaren2

def komtvoren(getallen, controleGetal1, controleGetal2):
    komtvoor = controleGetal1 in getallen and controleGetal2 in getallen
    return komtvoor

def vind_posities(getallen, controlegetal1):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def bereken_standaardafwijking(getallen):
    aantal = len(getallen)
    gemiddelde = sum(getallen) / aantal
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def shufflelijst(getallen):
    shuffle = random.shuffle(getallen)
    return shuffle

def randomgetal(getallen):
    aantal = len(getallen)
    randomgetalkiezen = getallen[random.randint(0,aantal-1)]
    return randomgetalkiezen 

def vershillen2(random_getal, controlegetal2):
    verschil2 = abs(random_getal - controlegetal2)
    return verschil2


