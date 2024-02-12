from fruitmand2 import fruitmand

fruitmand.sort(key=lambda x: x['weight'], reverse=True) #Sorteerd het gewicht op aflopende volgorde dus zwaar naar licht

for fruit in fruitmand:
    gewicht_kg = fruit['weight'] / 1000
    print(fruit['name'], gewicht_kg, 'kg')