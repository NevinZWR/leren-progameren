import random
mm_colors = ('oranje', 'blauw', 'groen', 'bruin')

aantal_mm = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))

zak_met_mm = []

for _ in range(aantal_mm):
    kleur = random.choice(mm_colors)
    zak_met_mm.append(kleur)

print("Inhoud van de zak met M&M's:")
print(zak_met_mm)
