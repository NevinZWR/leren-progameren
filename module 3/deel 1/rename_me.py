def checkEven(nummer:int) -> bool:
    return nummer % 2 == 0 # checkt of het nummer even is


def reversePrint(zin:str) -> str:
    zin2 = zin.split()
    omgekeerdezinmaken = zin2[::-1]
    omgekeerdezin = ' '.join(omgekeerdezinmaken)
    return omgekeerdezin
#print(reversePrint("een appel is gezond"))


def aantaluniekeletters(woorduniek:str) -> int:
    woord = set(woorduniek)
    uniekletter = len(woord)# telt unieke letters op
    return uniekletter
#print(aantaluniekeletters("abcdaa"))

def berekenwoordaantal(tekst:str)-> int:
    woorden = tekst.split()
    
    totalelengte = 0
    for woord in woorden:
        totalelengte += len(woord)

    gemiddeldelengte = int(totalelengte / len(woorden))
    return gemiddeldelengte

# print(verschillendeletters("sinaasappel"))

def tafelPrint(tafelgetal:int, getal:int=10) -> None:#print de tafels uit
    for getal2 in range(1, getal+1):
        uitkomst = getal2 * tafelgetal
        print(f'{getal2} x {tafelgetal} = {uitkomst}')
tafelPrint(5,40)