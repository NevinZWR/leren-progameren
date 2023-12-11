dagenvandeweek = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

print("Alle dagen van de week zijn:")
for dag in dagenvandeweek:
    print(dag)
print("\n")

print("De werkdagen zijn:")
for dag in dagenvandeweek[:5]:
    print(dag)
print("\n")

print("De weekenddagen zijn:")
for dag in dagenvandeweek[-2:]:
    print(dag)
print("\n")

print("Alle dagen van de week in omgekeerde volgorde zijn:")
for dag in reversed(dagenvandeweek):
    print(dag)
print("\n")

print("De werkdagen in omgekeerde volgorde zijn:")
for dag in reversed(dagenvandeweek[:5]):
    print(dag)
print("\n")

print("De weekenddagen in omgekeerde volgorde zijn:")
for dag in reversed(dagenvandeweek[-2:]):
    print(dag)
print("\n")
