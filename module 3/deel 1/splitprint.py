from splitfunctie import *
gegevens = verzamel_gegevens()
for person in gegevens:
    print(f"{person['name']}, die in {person['city']} woont, is {person['age']}")