from functies import *
from datapapi import *


print("Welkom bij Papi Gelato")
Again = True
ZakOfPar = ParticulierOfZakelijk()
while Again:
    Aantal = AantalBol(ZakOfPar)
    Smaakje = Smaak(Aantal, ZakOfPar)	
    Verpak = Verpakking(Aantal, ZakOfPar)
    if Verpak == 'bakje':
        Aantalbakjes += 1
    elif Verpak == 'hoorntje':
        Aantalhoorntjes += 1
    Topping = Toppings(Aantal, Verpak, ZakOfPar)
    if ZakOfPar == 'particulier':
     print(f'u krijgt van ons een {Verpak} met {Aantal} bolletje(s)')
    AantalIjs +=  Aantal
    Again = OrderAgain(JA, NEE, ZakOfPar)
Bonnetje(AantalIjs, Aantalbakjes, Aantalhoorntjes, Verpak, Topping, ZakOfPar)
