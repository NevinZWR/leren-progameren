a = int(input("Voer het eerste gehele getal in: "))
b = int(input("Voer het tweede gehele getal in: "))

Min = a
Max = b

if a > b:
    Max = a
    print("a is het grootste getal:", Max)
elif a < b:
    Min = a
    print("a is het kleinste getal:", Min)
else:
    print("a en b zijn even groot.")

print("Het minimum is:", Min)
print("Het maximum is:", Max)


