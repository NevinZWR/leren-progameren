import random

ja = ['ja', 'yes', 'y', 'j']
nee = ['n', 'no', 'nee']

max_rondes = 20
score = 0
ronde = 1

while True:
    geheim_getal = random.randint(1, 1000)
    print(f"--- Ronde {ronde} ---")
    print(geheim_getal)
    for poging in range(1, 11):
        try:
            nummer = int(input("Raad een getal tussen de 1 en de 1000: "))
        except ValueError:
            print("Ongeldige invoer. Voer een getal in")
            continue
        
        if nummer < 0:
            print("Voer een positief getal in.")

        if nummer == geheim_getal:
            print("Gefeliciteerd, je hebt het getal geraden!")
            score += 1
            break

        elif nummer < geheim_getal:
            print("Het ingevoerde getal is lager dan het geheime getal.")

        else:
            print("Het ingevoerde getal is hoger dan het geheime getal.")
            
        verschil = abs(nummer - geheim_getal)

        if verschil < 20:
            print("Je bent heel warm")
        elif verschil < 50:
            print("Je bent warm")

    print(f"Dit is je eindscore: {score}")

    doorgaan = input("Wil je nog een ronde spelen? (Ja/Nee): ").lower()
    if doorgaan in ja:
        ronde += 1
    else:
        print(f"Dit is je eindscore: {score}")
        break
