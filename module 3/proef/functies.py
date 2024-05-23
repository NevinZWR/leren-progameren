import sys
def AantalBol() -> int:
    while True:
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
            
def OrderAgain(ja: list, nee: list):
    while True:
        opnieuw = input("Wil je nog een keer bestellen? ").lower()
        if opnieuw in ja:
            pass
            break
        elif opnieuw in nee:
            print('Bedankt en tot ziens!')
            sys.exit()
            break
        else:
            print('Sorry, dat begreep ik niet')

def verpakking(aantalBolletjes: int) -> str:
            while True:
                if aantalBolletjes > 3:
                    return 'bakje'
                verpakking = input('Wil je deze in een bakje of hoorntje: ').lower()
                if verpakking == 'bakje':
                    return 'bakje'
                elif verpakking == 'hoorntje':
                    return 'hoorntje'
                else:
                    print('Sorry, dat begreep ik niet')



