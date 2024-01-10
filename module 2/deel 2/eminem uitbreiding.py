import random

mm_kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']
dictionary = {}

aantal_mm = int(input("Voer in hoeveel M&M's wil toevoegen"))

for i in range(aantal_mm):
    kleur = random.choice(mm_kleuren)
    if kleur in dictionary:
        dictionary[kleur] += 1
    else:
        dictionary[kleur] = 1
    
print(dictionary)