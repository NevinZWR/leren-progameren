def leeftijdennaam():
    while True:
        try:
            naam = input("Wat is uw naam? ").capitalize()
            leeftijd = int(input("Wat is uw leeftijd? "))
            print(f"{naam} is {leeftijd} jaar")
            break
        except ValueError:
            print("fout invoer voor uw naam en/of leeftijd(getal)")

leeftijdennaam()
