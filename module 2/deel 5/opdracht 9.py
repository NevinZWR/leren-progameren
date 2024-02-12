from fruitmand2 import fruitmand

fruitmand = [fruit for fruit in fruitmand if fruit['name'] != 'druif']

kleuren = set(fruit['color'] for fruit in fruitmand)#zorgt dat het niet dubbel print 

for kleur in kleuren:
    print(kleur)
