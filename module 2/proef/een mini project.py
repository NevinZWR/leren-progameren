import random

namen = []
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

lootjes = namen.copy()
random.shuffle(lootjes)

while True:
    if any(lootjes[i] == namen[i] for i in range(len(namen))):
        random.shuffle(lootjes)
    else:
        break

print("Namen en bijbehorende lootjes:")
for i in range(len(namen)):
    print(f"{namen[i]} - {lootjes[i]}")