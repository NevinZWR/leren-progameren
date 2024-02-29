def checkEven(nummer:int) -> bool:
    return nummer % 2 == 0 # checkt of het nummer even is
# print(quantum_broodrooster(4))

def reversePrint(zin:str) -> str:
    zin2 = zin.split()
    omgekeerdezinmaken = zin2[::-1]
    omgekeerdezin = ' '.join(omgekeerdezinmaken)
    return omgekeerdezin
# print(reversePrint("een appel is gezond"))


def aantaluniekeletters(woorduniek:str) -> int:
    woord = set(woorduniek)
    uniekletter = len(woord)# telt unieke letters op
    return uniekletter
#print(aantaluniekeletters("abcd"))

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def tafelPrint(tafelgetal:int, getal:int=10) -> None:#print de tafels uit
    for getal2 in range(1, getal+1):
        uitkomst = getal2 * tafelgetal
        print(f'{getal2} x {tafelgetal} = {uitkomst}')
 