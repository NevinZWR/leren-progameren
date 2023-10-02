croissant = int(input("hoeveel croissaints wilt u? "))
prijs_croissant = float(input("hoe duur zijn de croissaintjes? "))
stokbrood = int(input("hoeveel stokbroden wilt u? "))
prijs_stokbrood = float(input("hoe duur zijn de stokbroden? "))
aantalKortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u? "))
korting_waarde = float(input("hoeveel waarde heeft u kortingsbon in euro? "))

totaal_korting = aantalKortingsbonnen * korting_waarde
prijs_croissant = croissant * prijs_croissant
stokbrood_totaal = stokbrood * prijs_stokbrood
totaal = stokbrood_totaal + prijs_croissant - totaal_korting


print("De feestlunch kost je bij de bakker", totaal ,)
