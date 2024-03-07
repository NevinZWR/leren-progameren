from splitfunctie import *
gegevens = verzamel_gegevens()
for person in gegevens:
    print(f"in {person['city']} woont {person['age']} jarige {person['name']}")