from fruitmand import fruitmand

kleuren_vertaling = {
    'red': 'rode',
    'green': 'groene',
    'yellow': 'gele',
    'orange': 'oranje',
    'purple': 'paarse',
    'pink': 'roze'
}

# Vind het fruit met de langste naam
langste_fruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

kleur = kleuren_vertaling.get(langste_fruit['color'], langste_fruit['color'])

print(f"De {langste_fruit['name']} ({len(langste_fruit['name'])} letters) heeft een {kleur} kleur en een gewicht van {langste_fruit['weight']}g")