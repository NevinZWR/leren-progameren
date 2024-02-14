import random

namen = []
while True:
    naam = input("Voer een naam in (of typ 'stop' om te stoppen): ")
    if naam.lower() == 'stop':
        if len(namen) < 3:
            print("Er moeten minstens 3 namen worden ingevoerd.")
            continue
        else:
            break
    if naam not in namen:
        namen.append(naam)
    else:
        print("Deze naam is dubbel, vul een andere unieke naam in")

lootjes = namen.copy()
random.shuffle(lootjes)
while True:
    lootjes == namen for i in range
print("Namen en bijbehorende lootjes:")
for i in range(len(namen)):
    print(f"{namen[i]} - {lootjes[i]}")
