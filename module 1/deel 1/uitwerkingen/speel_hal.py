aantal_mensen = 4
prijs_toegang = 7.45
vip_5min  = 0.37
aantal_vip = 9
# aantal_minvip = 45
totaal_toegang = aantal_mensen * prijs_toegang
prijs_vip = vip_5min * aantal_vip

totaal = prijs_vip + totaal_toegang

print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar", totaal ,"euro")