boodschappenlijst = {}
while True:
        item = input("welkeproduct wilt u toevoegen (type stop om te eindigen) ").lower()

        if item == 'stop':
            break

        hoeveelheid = input("Voer de hoeveelheid in: ")

        # Controleer of het item al in de lijst staat
        if item in boodschappenlijst:
            boodschappenlijst[item] += int(hoeveelheid)
        else:
            boodschappenlijst[item] = int(hoeveelheid)

    # Toon de boodschappenlijst aan de gebruiker
print("\nBoodschappenlijst:")
for item, hoeveelheid in boodschappenlijst.items():
        print(f"{hoeveelheid}x {item}")
