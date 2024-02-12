from fruitmand import fruitmand

beschikbare_kleuren = set(fruit['color'] for fruit in fruitmand)
while True:
    gekozen_kleur = input("Kies een kleur uit " + ", ".join(beschikbare_kleuren) + ": ").lower()
    if gekozen_kleur in beschikbare_kleuren:
        break
    else:
        print(f"De kleur {gekozen_kleur} zit niet in de fruitmand.")

aantal_ronde_vruchten = sum(1 for fruit in fruitmand if fruit['color'] == gekozen_kleur and fruit['round'])
aantal_niet_ronde_vruchten = sum(1 for fruit in fruitmand if fruit['color'] == gekozen_kleur and not fruit['round'])

verschil = aantal_ronde_vruchten - aantal_niet_ronde_vruchten

if verschil > 0:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet-ronde vruchten in de kleur {gekozen_kleur}.")
elif verschil < 0:
    print(f"Er zijn {verschil * -1} minder ronde vruchten dan niet-ronde vruchten in de kleur {gekozen_kleur}.")
else:
    print(f"Er zijn evenveel ronde als niet-ronde vruchten in de kleur {gekozen_kleur}.")
