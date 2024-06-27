import sys
from datapapi import *
def AantalBol(ZakOfPar) -> int:
    while True:
        if ZakOfPar == 'particulier':
            try:
                aantalBolletjes = int(input('hoeveel bolletjes wil je? '))
                if aantalBolletjes <= 0:
                    print('wij tolereren geen grappenmakers hier')
                elif aantalBolletjes > 8:
                    print('Sorry, zulke grote bakken hebben we niet')
                elif aantalBolletjes >= 1:
                    return aantalBolletjes
            except ValueError:
                print('Ongeldige invoer. Voer alstublieft een geldig aantal bolletjes in.')
        elif ZakOfPar == 'zakelijk':
            try:
                aantalliter = int(input('hoeveel liter ijs wilt u? '))
                return aantalliter
            except ValueError:
                print('Ongeldige invoer. Voer alstublieft een geldig aantal liter in.')

def Smaak(AantalIjs, ZakOfPar: str ,) -> str:
    for i in range(AantalIjs):
        while True:
            if ZakOfPar == 'particulier':
                smaak = input(f'Welke smaak wilt u voor bolletje nummer {i + 1}? A) Aardbei, C) Chocolade of V) Vanille?').upper()
            elif ZakOfPar == 'zakelijk':
                smaak = input(f'Welke smaak wilt u voor liter nummer {i + 1}? A) Aardbei, C) Chocolade of V) Vanille?').upper()
            if smaak == 'A':
                Smaken['Aardbei'] += 1
                break                
            elif smaak == 'C':
                Smaken['Chocolade'] += 1
                break
            elif smaak == 'V':
                Smaken['Vanille'] += 1
                break    

            else:
                print('Sorry dat is geen optie die we aanbieden...')

def Toppings(aantalbolletjes: int, Verpakking: str, ZakOfPar):
        while True:
            if ZakOfPar == 'zakelijk':
                break
            Topping = input('Wat voor topping wilt u: G) Geen, SL) Slagroom, S) Sprinkels of C) Caramel Saus?').upper()
            if Topping == 'G':
                break
            elif Topping == 'SL':
                Toppingen['Slagroom'] += 1
                break
            elif Topping == 'S':
                Toppingen['Sprinkels'] += aantalbolletjes
                break
            elif Topping == 'C' and Verpakking == 'bakje':
                Toppingen['CaramelBakje'] += 1
                break
            elif Topping == 'C' and Verpakking == 'hoorntje':
                Toppingen['CaramelHoorntje'] += 1
                break
               
            else:
                print('Sorry dat is geen optie die we aanbieden...')
            
def OrderAgain(ja: list, nee: list, ZakOfPar: str) -> bool:
    if ZakOfPar == 'zakelijk':
        return False
    while True:
        opnieuw = input("Wil je nog een keer bestellen? ").lower()
        if opnieuw in ja:
            return True
        elif opnieuw in nee:
           return False
        else:
            print('Sorry, dat begreep ik niet')

def Verpakking(aantalBolletjes: int, ZakOfPar: str) -> str:
            while True:
                if ZakOfPar == 'zakelijk':
                    break
                elif aantalBolletjes > 3:
                    return 'bakje'
                verpakking = input('Wil je deze in een B) bakje of H) hoorntje: ').lower()
                if verpakking == 'b':
                    return 'bakje'
                elif verpakking == 'h':
                    return 'hoorntje'
                else:
                    print('Sorry dat is geen optie die we aanbieden...')
def Bonnetje(aantalBolletjes: int, aantalbakjes: int, aantalhoorntjes: int, verpakkingen: str, toppings:str , ZakOfPar: str):
    print("-------Papi Gelato-------")
    if ZakOfPar == 'particulier':
        for Smaak in Smaken:
            if Smaken[Smaak] > 0:
                print(f"B.{Smaak}      {Smaken[Smaak]} x 0.95 = {Smaken[Smaak] * 0.95:.2f} euro") 
        if aantalbakjes > 0:
            print(f"Bakjes      {aantalbakjes} x 0.75 = {aantalbakjes * 0.75:.2f} euro")
        if aantalhoorntjes > 0:
            print(f"Hoorntjes   {aantalhoorntjes} x 1.25 = {aantalhoorntjes * 1.25:.2f} euro")
        if len(Toppingen) > 0:
            toppingprijs = Toppingen['Slagroom'] * 0.50 + Toppingen['CaramelBakje'] * 0.90 + Toppingen['CaramelHoorntje'] * 0.60 + Toppingen['Sprinkels'] * 0.30
        print(f"Topping                   = {toppingprijs:.2f}")
        print(f"Totale                = {aantalBolletjes * 0.95 + aantalbakjes * 0.75 + aantalhoorntjes * 1.25 + toppingprijs:.2f} euro")
    elif ZakOfPar == 'zakelijk':
        for Smaak in Smaken:
            if Smaken[Smaak] > 0:
                print(f"L.{Smaak}      {Smaken[Smaak]} x 9.80 = {Smaken[Smaak] * 9.80:.2f} euro") 
        print(f"Totale                = {aantalBolletjes * 9.80:.2f} euro")
        print(f"BTW (6%)           = {(aantalBolletjes * ((9.80 * 6) / 106)) * 0.06:.2f} euro")
    print('Bedankt en tot ziens!')

def ParticulierOfZakelijk() -> str:
    while True:
        soort = input('Bent u een P) particuliere of Z) zakelijke klant? ').upper()
        if soort == 'P':
            return 'particulier'
        elif soort == 'Z':
            return 'zakelijk'
        else:
            print('Sorry, dat begreep ik niet')