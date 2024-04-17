def maakReeks():
    reeks = ["1"]
    print(reeks[0]) # print de eerste waarde
    while True:
        waarde = reeks[-1] # pak de laatste waarde
        volgendeReeks = "" # maak een lege string omdat de volgende reeks gaan maken
        count = 1 # zet de count op 1
        for i in range(1, len(waarde)): 
            if waarde[i] == waarde[i - 1]: # als de huidige waarde gelijk is aan de vorige waarde
                count += 1 # tel 1 bij de count op
            else:
                volgendeReeks += str(count) + waarde[i - 1] # voeg de count en de waarde toe aan de volgende reeks
                count = 1 # zet de count weer op 1
        volgendeReeks += str(count) + waarde[-1] # voeg de count en de laatste waarde toe aan de volgende sequentie
        reeks.append(volgendeReeks) # voeg de volgende reeks toe aan de lijst
        print(volgendeReeks)
        if "33" in volgendeReeks:
            break

maakReeks()
