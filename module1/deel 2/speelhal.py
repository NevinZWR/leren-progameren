aantal_mensen = int(input("met hoeveel mensen zijn jullie? "))
prijs_toegang = float(input("hoeveel is de toegangs prijs? "))
vip_5min  = float(input("hoeveel kost de VIP per 5 minuten? "))
aantal_vip = int(input("hoeveel keer wilt u 5 minuten VIP? "))

totaal_toegang = aantal_mensen * prijs_toegang
prijs_vip = vip_5min * aantal_vip

totaal = prijs_vip + totaal_toegang

print("De totale prijs voor de speelhal inclusief VIP is", totaal,)

