def leeftijdennaam():
    naam = input("Wat is uw naam? ").capitalize()
    while True:
        try:            
            leeftijd = int(input("Wat is uw leeftijd? "))
            print(f"{naam} is {leeftijd} jaar")
            break
        except ValueError:
            print("fout invoer voor uw leeftijd(getal)")

leeftijdennaam()
