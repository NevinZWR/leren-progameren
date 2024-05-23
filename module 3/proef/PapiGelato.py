from functies import *
from datapapi import *

ja = ['ja', 'yes', 'y', 'j']
nee = ['nee', 'no', 'n']

print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
while True:
    aantalbol = AantalBol()
    verpak = verpakking(aantalbol)
    print(f'u krijgt van ons een {verpak} met {aantalbol} bolletje(s) vanille ijs')
    OrderAgain(ja, nee)






# while True:
#     try:
#         aantalBolletjes = int(input('hoeveel bolletjes wil je? '))
#         if aantalBolletjes <= 0:
#             print('wij tolereren geen grappenmakers hier')
#         elif aantalBolletjes <= 3:
#             while True:
#                 verpakking = input('Wil je deze in een bakje of hoorntje: ').lower()
#                 if verpakking == 'bakje':
#                     print(f'u krijgt van ons een bakje met {aantalBolletjes} bolletje(s) vanille ijs')
#                     OrderAgain(ja, nee)
#                     break
#                 elif verpakking == 'hoorntje':
#                     print(f'u krijgt van ons een hoorntje met {aantalBolletjes} bolletje(s) vanille ijs')
#                     OrderAgain(ja, nee)
#                     break
#                 else:
#                     print('Sorry, dat begreep ik niet')
#         elif aantalBolletjes > 8:
#             print('Sorry, zulke grote bakken hebben we niet')
#         elif aantalBolletjes > 3:
#             print(f'u van ons een bakje met {aantalBolletjes} bolletjes vanille ijs')
#             OrderAgain(ja, nee)
#     except ValueError:
#         print('Ongeldige invoer. Voer alstublieft een geldig aantal bolletjes in.')