import random

namen = []
cadeautjes = {}
while True:
    naam = input("Voer een naam in (of typ 'stop' om te stoppen): ").lower()
    if naam == 'stop':
        if len(namen) < 3:
            print("Er moeten minstens 3 namen worden ingevoerd.")
            continue
        else:
            break
    if naam in namen:
        print("Deze naam is al ingevoerd. Vul een andere unieke naam in.")
        continue
    
    namen.append(naam)
    cadeautjes[naam] = []
    for i in range(3):
        cadeautje = input(f"Voer cadeautje {i+1} in voor {naam}: ")
        cadeautjes[naam].append(cadeautje)

lootjes = namen.copy()
random.shuffle(lootjes)

while True:
    if any(lootjes[i] == namen[i] for i in range(len(namen))):
        random.shuffle(lootjes)
    else:
        break

dict_lootjes = dict(zip(namen, lootjes))

while True:
    zoek_naam = input("voer je naam in om je lootje te zien(voer 'stop' in om the stoppen)").lower()
    if zoek_naam == "stop":
        break
    if zoek_naam in dict_lootjes:
        print(f"{zoek_naam} heeft lootje: {dict_lootjes[zoek_naam]} zijn verlanglijsje is {cadeautjes[dict_lootjes[zoek_naam]]}")
    else:
        print("die naam is er niet")