import random

def raden_spel():
    eindscore = 0
    max_ronden = 20
    geheim_getal = random.randint(1, 1000)

    for ronde in range(1, max_ronden + 1):
        print(f"\n--- Ronde {ronde} ---")
        score = 0

        for x in range(1, 11):
            nummer = int(input("Doe een gok tussen 1 en 1000: "))

            verschil = abs(geheim_getal - nummer)

            if nummer == geheim_getal:
                print("Gefeliciteerd! Je hebt het juiste getal geraden.")
                score += 1
                break
            elif verschil < 20:
                print("Je bent heel warm.")
            elif verschil < 50:
                print("Je bent warm.")
            elif nummer < geheim_getal:
                print("Hoger.")
            else:
                print("Lager.")

        eindscore += score
        print(f"Score tot nu toe: {eindscore}")

        if ronde < max_ronden:
            opnieuw_spelen = input("Nog een getal raden? (ja/nee): ").lower()
            if opnieuw_spelen != 'ja':
                break

    print(f"Eindscore: {eindscore}")

if __name__ == "__main__":
    raden_spel()
