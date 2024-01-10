import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
deck = ['joker' , 'joker']
for kleur in kleuren:
    for waarde in waarden:
        deck.append(kleur + ' ' + waarde)
   
random.shuffle(deck)
print(deck)
print('----')
for j in range(7):
    print(f'kaart {j + 1}' , deck.pop(0))
print('----')
print('deck' , len(deck))
print(deck)