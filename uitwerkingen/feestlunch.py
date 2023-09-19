croissant = 17
aantal_croissant = 0.39
stokbrood = 2
prijs_stokbrood = 2.78
kortingsbon = 3
korting_waarde = 0.50

kosten_crossaint = croissant * aantal_croissant
kosten_stokbrood = stokbrood * prijs_stokbrood
totaalwaarde_korting = kortingsbon * korting_waarde

totale_kosten = kosten_crossaint + kosten_stokbrood - totaalwaarde_korting
print("het totaal komt uit op:", totale_kosten)