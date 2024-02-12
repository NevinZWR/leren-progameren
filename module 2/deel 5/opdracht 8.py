from fruitmand2 import fruitmand

watermeloen = {
    'name': 'watermeloen',
    'weight': 3000,
    'color': 'green',
    'round': True
}

fruitmand.append(watermeloen)
totale_gewicht = sum(fruit['weight'] for fruit in fruitmand)

print("Totale gewicht van de fruitmand:", totale_gewicht)
