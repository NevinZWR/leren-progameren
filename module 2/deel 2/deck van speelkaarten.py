import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
deck = [(waarde, kleur) for kleur in kleuren for waarde in waarden]

deck.extend([('joker', 'joker')] * 2)

random.shuffle(deck)

print("Bovenste 7 kaarten:")
print(deck[:7])

print("\nOverige kaarten in het deck:")
print(deck[7:])
