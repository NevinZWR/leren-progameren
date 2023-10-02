a = int(input("Voer het eerste gehele getal in: "))
b = int(input("Voer het tweede gehele getal in: "))

# Controleer welk getal groter is met behulp van een if-statement
if a > b:
    Max = a
    print("a is het grootste getal:", Max)
elif a < b:
    Min = a
    print("a is het kleinste getal:", Min)