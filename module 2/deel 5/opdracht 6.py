from fruitmand2 import fruitmand
gewicht = [fruit['weight'] for fruit in fruitmand if fruit['name'] == 'appel'][0]
print(gewicht)