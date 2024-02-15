def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'

nr1 = int(input("Voer het eerste gehele getal in: "))
nr2 = int(input("Voer het tweede gehele getal in: "))
resultaat = vergelijk_getallen(nr1, nr2)

print(resultaat)

