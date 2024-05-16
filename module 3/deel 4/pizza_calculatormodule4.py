from functions import *

pizzas = {
    'small': {'amount': 0, 'price': 8.99},
    'medium': {'amount': 0, 'price': 12.99},
    'large': {'amount': 0, 'price': 15.99}
}

for pizza in pizzas:
    pizzas[pizza]['amount'] = get_integer_input(f"Hoeveel {pizza} pizza's wilt u? ")

for pizza in pizzas: 

    total = pizzas[pizza]['amount'] * pizzas[pizza]['price']
    print(f'u heeft totaal van {pizzas[pizza]["amount"]} {pizza} pizza\'s = €{total}')
totale_prijs = sum([pizzas[pizza]['amount'] * pizzas[pizza]['price'] for pizza in pizzas])
print(f'De totale prijs is €{totale_prijs}')