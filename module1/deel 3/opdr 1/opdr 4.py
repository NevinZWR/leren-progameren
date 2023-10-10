a = int(input("Voer het eerste gehele getal in: "))
b = int(input("Voer het tweede gehele getal in: "))

if a > b:
    Max = a
    Min = b
    print("a is het grootste getal:", Max)
elif a < b:
    Min = a
    Max = b
    print("a is het kleinste getal:", Min)
else:
    Min = Max = a
    print("a en b zijn even groot.")


print("Het minimum is:", Min)
print("Het maximum is:", Max)


