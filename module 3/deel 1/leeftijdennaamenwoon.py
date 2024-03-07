def verzamel_gegevens():
    gegevens = []
    while True:
        doorgaan = input("Toets iets om door te gaan of stop om te printen: ")
        if doorgaan.lower() == 'stop':
            break
        while True:
            try:
                naam = input("Wat is uw naam? ").capitalize()
                leeftijd = int(input("Wat is uw leeftijd? "))
                woonplaats = input("wat is uw woonplaats? ").capitalize()
                gegevens.append({'name': naam, 'age': leeftijd, 'city': woonplaats})
                break
            except ValueError:
                print("Ongeldige invoer voor leeftijd. Voer een geldig geheel getal in.")
    return gegevens

gegevens = verzamel_gegevens()
for person in gegevens:
    print(f"{person['name']}, die in {person['city']} woont, is {person['age']}")